#!/usr/bin/env ruby
# frozen_string_literal: true

# Checks the front matter of _impls/*.md for mistakes the Jekyll build
# accepts silently: Liquid renders a misspelt key as nothing, and YAML keeps
# only the last of two equal keys.
#
# Usage: ruby validate-data.rb     (exits non-zero if anything is wrong)

require 'yaml'
require 'date'

ROOT = File.dirname(File.expand_path(__FILE__))

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

classes = load_yaml('_data/proto_classes.yml').keys

errors = []

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
end

if errors.empty?
  puts 'Data files OK.'
else
  warn errors
  exit 1
end
