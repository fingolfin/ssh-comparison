#!/usr/bin/env ruby
# frozen_string_literal: true

# Checks the front matter of _impls/*.md for mistakes the Jekyll build
# accepts silently: Liquid renders a misspelt key, platform or language as
# nothing, and YAML keeps only the last of two equal keys. Vocabularies for the
# implementation metadata are in _data/impl_meta.yml.
#
# Usage: ruby validate-data.rb     (exits non-zero if anything is wrong)

require 'yaml'
require 'date'

ROOT = File.dirname(File.expand_path(__FILE__))

# `no` is false in YAML 1.1, which Psych follows.
SIDES = { 'client' => %w[client], 'server' => %w[server],
          'both' => %w[client server], false => [] }.freeze

def load_yaml(path)
  YAML.safe_load_file(File.join(ROOT, path), permitted_classes: [Date])
end

# Front matter source only; the body after the closing --- is prose.
def front_matter_text(path)
  text = File.read(path, encoding: 'UTF-8')
  m = text.match(/\A---\s*\n(.*?)\n---\s*\n/m)
  m && m[1]
end

# Keys given twice in one mapping, anywhere below node.
def duplicate_keys(node, prefix = '', out = [])
  case node
  when Psych::Nodes::Mapping
    pairs = node.children.each_slice(2).to_a
    pairs.map { |k, _| k.value }.tally.each { |k, n| out << "#{prefix}#{k}" if n > 1 }
    pairs.each { |k, v| duplicate_keys(v, "#{prefix}#{k.value}.", out) }
  when Psych::Nodes::Sequence
    node.children.each { |c| duplicate_keys(c, prefix, out) }
  end
  out
end

# Active list items of the protocols block, as [class, id, comment].
def protocol_items(source)
  items = []
  cls = nil
  in_protocols = false
  source.each_line do |line|
    if line =~ /^\S/
      in_protocols = line.start_with?('protocols:')
      next
    end
    next unless in_protocols

    if line =~ /^\s+(\w+):\s*$/
      cls = Regexp.last_match(1)
      next
    end
    m = line.match(/^\s+- (\S+)\s*(?:#(.*))?$/) or next
    items << [cls, m[1], m[2].to_s]
  end
  items
end

# A protocols comment that says the id is off by default.
DEFAULT_OFF_COMMENT = /\b(disabled by default|not in the default proposal|not default)\b/i

classes   = load_yaml('_data/proto_classes.yml').keys
meta      = load_yaml('_data/impl_meta.yml')
platforms = meta['platforms'].keys
languages = meta['languages']

errors = []
warnings = []

Dir[File.join(ROOT, '_impls', '*.md')].sort.each do |path|
  name = File.basename(path)
  source = front_matter_text(path)
  if source.nil?
    errors << "#{name}: no YAML front matter"
    next
  end
  fm = YAML.safe_load(source, permitted_classes: [Date]) || {}

  duplicate_keys(YAML.parse(source).root).each do |key|
    errors << "#{name}: #{key} given twice; YAML keeps only the last"
  end

  # Sides the entry claims to implement.
  claimed = []
  %w[client server].each do |side|
    next unless fm.key?(side)

    value = fm[side]
    errors << "#{name}: #{side}: #{value.inspect} is not yes or no" unless [true, false].include?(value)
    claimed << side if value == true
  end

  # standalone and library: what each covers, and together exactly the claim.
  covered = {}
  %w[standalone library].each do |key|
    next unless fm.key?(key)

    value = fm[key]
    unless SIDES.key?(value)
      errors << "#{name}: #{key}: #{value.inspect} is not one of client, server, both, no"
      next
    end
    covered[key] = SIDES[value]
    extra = SIDES[value] - claimed
    errors << "#{name}: #{key} covers #{extra.join(', ')}, which client/server do not claim" unless extra.empty?
  end
  if covered.size == 2
    missing = claimed - covered.values.flatten
    errors << "#{name}: neither standalone nor library covers #{missing.join(', ')}" unless missing.empty?
  end

  if fm.key?('platforms')
    list = fm['platforms']
    if !list.is_a?(Array) || list.empty?
      errors << "#{name}: platforms must be a non-empty list; leave it out if unknown"
      list = []
    end
    (list - platforms).each do |p|
      errors << "#{name}: platform #{p.inspect} is not one of #{platforms.join(', ')}"
    end
    other = fm['platforms-other']
    if list.include?('other') && (other.nil? || other.to_s.strip.empty?)
      errors << "#{name}: platform other needs a platforms-other note"
    elsif !list.include?('other') && fm.key?('platforms-other')
      errors << "#{name}: platforms-other given without other in platforms"
    end
  elsif fm.key?('platforms-other')
    errors << "#{name}: platforms-other given without platforms"
  end

  if fm.key?('languages')
    list = fm['languages']
    if !list.is_a?(Array) || list.empty?
      errors << "#{name}: languages must be a non-empty list; leave it out if unknown"
      list = []
    end
    (list - languages).each do |lang|
      errors << "#{name}: language #{lang.inspect} is not in _data/impl_meta.yml"
    end
  end

  # protocols: class => list of algorithm ids. A class with no list (only a
  # comment under it) means none are supported.
  protocols = fm['protocols']
  unless protocols.is_a?(Hash)
    errors << "#{name}: protocols must be a map of class to list"
    next
  end
  (protocols.keys - classes).each do |cls|
    errors << "#{name}: protocols: class #{cls.inspect} is not one of #{classes.join(', ')}"
  end
  protocols.each do |cls, ids|
    next if ids.nil?

    unless ids.is_a?(Array) && ids.all?(String)
      errors << "#{name}: protocols.#{cls} must be a list of ids"
      next
    end
    ids.tally.each { |id, n| errors << "#{name}: protocols.#{cls}: #{id} listed #{n} times" if n > 1 }
  end

  # disabled-by-default: class => ids that are supported but off unless
  # configured, so each must also be in the matching protocols list. A
  # comment alone only warns, so entries that predate the key still build.
  off = fm['disabled-by-default'] || {}
  unless off.is_a?(Hash)
    errors << "#{name}: disabled-by-default must be a map of class to list"
    next
  end
  (off.keys - classes).each do |cls|
    errors << "#{name}: disabled-by-default: class #{cls.inspect} is not one of #{classes.join(', ')}"
  end
  off.each do |cls, ids|
    unless ids.is_a?(Array) && ids.all?(String)
      errors << "#{name}: disabled-by-default.#{cls} must be a list of ids"
      next
    end
    ids.tally.each { |id, n| errors << "#{name}: disabled-by-default.#{cls}: #{id} listed #{n} times" if n > 1 }
    (ids - (protocols[cls] || [])).each do |id|
      errors << "#{name}: disabled-by-default.#{cls}: #{id} is not in protocols.#{cls}"
    end
  end

  protocol_items(source).each do |cls, id, comment|
    next unless comment =~ DEFAULT_OFF_COMMENT
    next if Array(off[cls]).include?(id)

    warnings << "#{name}: protocols.#{cls}: #{id} is commented as off by default " \
                "but not in disabled-by-default.#{cls}"
  end

  # help-wanted: the reason shown in the entry's notice. A bare `yes` would
  # render as "true".
  next unless fm.key?('help-wanted')

  reason = fm['help-wanted']
  next if reason.is_a?(String) && !reason.strip.empty?

  errors << "#{name}: help-wanted must say what needs recording"
end

warn(warnings.map { |w| "warning: #{w}" }) unless warnings.empty?

if errors.empty?
  puts 'Data files OK.'
else
  warn errors
  exit 1
end
