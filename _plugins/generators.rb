module Jekyll

  class SSHComparisonPage < Page
    def initialize(site)
      @site = site
      @dir = ''
      @name = "comparison.html"
      self.process(@name)       # splits @name into @ext and @basename

      specs = site.data['specs']
      impls_list = site.collections['impls'].docs
      impls = {}
      impls_list.each do |impl|
        impls[impl.basename_without_ext] = impl.data
      end

      self.content = ""

      # Create tables of all known protocols
      protocols = {}
      site.data['proto_classes'].each do |proto_class, proto_class_desc|
        proto_info = {}

        specs.each do |spec_id, spec|
          next unless spec.has_key?('protocols')
          next unless spec['protocols'].has_key?(proto_class)
          list = spec['protocols'][proto_class]
          list.each do |proto_name|
            p = proto_info.fetch(proto_name, {"spec" => nil, "impls" => {}})
            p['spec'] = spec
            proto_info[proto_name] = p
          end
        end

        # Record for each implementation which protocols its supports
        # in this protocol class
        impls.each do |impl_name, impl|
          next unless impl['protocols'].has_key?(proto_class)
          list = impl['protocols'][proto_class]
          next if list.nil?
          list.each do |proto_name|
            p = proto_info.fetch(proto_name, {"spec" => nil, "impls" => {}})
            p['impls'][impl_name] = true
            proto_info[proto_name] = p
          end
        end

        # For implementations for which we have no information about this
        # protocol class, record the support as "unknown"
        impls.each do |impl_name, impl|
          next if impl['protocols'].has_key?(proto_class)
          proto_info.each do |proto_name, proto_desc|
            proto_desc['impls'][impl_name] = "unknown"
          end
        end

        self.content << "<h3 class='post-header'>#{proto_class_desc}</h3>\n"
        self.content << "<div class='post-content'>\n"
        output_table(proto_class, proto_info, specs, impls)
        self.content << "</div>\n"
      end

      self.data = {
           'layout' => 'default',
           'title' => 'The comparison',
           'generated' => true,
       }
    end

    def output_table(proto_class, proto_info, specs, impls)
      table_id = "cmp-table-#{proto_class}"
      self.content << "<table id='#{table_id}' class='impl-comparison tablesorter table-header-rotated'>\n"

      impls_sorted = impls.sort_by {|k,v| v["title"].downcase}
      protos_sorted = proto_info.sort_by {|k,v| k}

      # Table head
      self.content << "<thead><tr><th>id</th>\n"
      self.content << "  <th class=\"rotate\"><div><span>Specification</span></div></th>\n"
      impls_sorted.each do |impl_name, impl|
        self.content << "  <th class=\"rotate\"><div><span><a href=\"/impls/#{impl_name}.html\">#{impl['title']}</a></span></div></th>\n"
      end
      self.content << "</tr></thead>\n"

      # Body
      self.content << "<tbody>\n"

      protos_sorted.each do |proto_name, proto_desc|
        self.content << "<tr>\n"
        self.content << "  <td>#{proto_name}</td>\n"

        # link to specification, if any
        spec = proto_desc.fetch('spec', nil)
        unless spec.nil?
          self.content << "  <td><a href=\"#{spec['url']}\">#{spec['name']}</a></td>\n"
        else
          self.content << "  <td></td>\n"
        end

        # TODO: iterate over impls_sorted
        impls_sorted.each do |impl_name, impl|
          if proto_desc['impls'].has_key?(impl_name)
            if proto_desc['impls'][impl_name] == "unknown"
              self.content << "  <td class=\"unknown\">?</td>"
            else
              self.content << "  <td class=\"yes\">Yes</td>  "
            end
          else
              self.content << "  <td class=\"no\">No</td>    "
          end
          self.content << "  <!-- #{impl_name} -->\n"
        end

        self.content << "</tr>\n"
      end

      self.content << "</tbody>\n"
      self.content << "</table>\n"

    end
  end

  class SSHComparisonPageGenerator < Generator
    safe true

    def generate(site)
      site.pages << SSHComparisonPage.new(site)
    end
  end

end
