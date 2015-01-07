module Jekyll

  class SSHImplementationPage < Page
    def initialize(site, name, desc)
      @desc = desc
      @site = site
      @dir = 'impls'
      @name = "#{name}.html"
      self.process(@name)       # splits @name into @ext and @basename

      self.content = ''
      self.data = {
         'layout' => 'impl',
         'impl' => desc,
         'title' => desc['name'],
         'generated' => true,
       }
    end
  end

  class SSHImplementationPageGenerator < Generator
    safe true

    def generate(site)
      dir = site.config['category_dir'] || 'categories'
      site.data['impls'].each do |name, desc|
        site.pages << SSHImplementationPage.new(site, name, desc)
      end
    end
  end

  class SSHComparisonPage < Page
    def initialize(site)
      @site = site
      @dir = ''
      @name = "comparison.html"
      self.process(@name)       # splits @name into @ext and @basename

      rfcs = site.data['rfcs']
      impls = site.data['impls']

      self.content = ""

      # Create tables of all known protocols
      protocols = {}
      site.data['proto_classes'].each do |proto_class, proto_class_desc|
        proto_info = {}

        rfcs.each do |rfc|
          next unless rfc['protocols'].has_key?(proto_class)
          list = rfc['protocols'][proto_class]
          list.each do |proto_name|
            p = proto_info.fetch(proto_name, {"rfc" => nil, "impls" => {}})
            p['rfc'] = rfc['rfc']
            proto_info[proto_name] = p
          end
        end

        impls.each do |impl_name, impl|
          next unless impl['protocols'].has_key?(proto_class)
          list = impl['protocols'][proto_class]
          next if list.nil?
          list.each do |proto_name|
            p = proto_info.fetch(proto_name, {"rfc" => nil, "impls" => {}})
            p['impls'][impl_name] = true
            proto_info[proto_name] = p
          end
        end

        self.content << "<h3 class='post-header'>#{proto_class_desc}</h3>\n"
        self.content << "<div class='post-content'>\n"
        output_table(proto_class, proto_info, rfcs, impls)
        self.content << "</div>\n"
      end

      self.data = {
           'layout' => 'default',
           'title' => 'The comparison',
           'generated' => true,
       }
    end

    def output_table(proto_class, proto_info, rfcs, impls)
      self.content << "<table class='impl-comparison'>"

      impls_sorted = impls.sort_by {|k,v| v["name"].downcase}
      protos_sorted = proto_info.sort_by {|k,v| k}

      # Table head
      self.content << "<thead><tr><th></th>"
      self.content << "<th>RFC?</th>"
      impls_sorted.each do |impl_name, impl|
        self.content << "<th><a href='impls/#{impl_name}.html'>#{impl['name']}</a></th>"
      end
      self.content << '</tr></thead>'

      # Body
      self.content << "<tbody>"

      protos_sorted.each do |proto_name, proto_desc|
        self.content << "<tr>"
        self.content << "<td>#{proto_name}</td>"

        # link to RFC, if any
        if proto_desc.has_key?('rfc')
          self.content << "<td><a href='https://tools.ietf.org/html/rfc#{proto_desc['rfc']}'>#{proto_desc['rfc']}</a></td>"
        else
          self.content << "<td></td>"
        end

        # TODO: iterate over impls_sorted
        impls_sorted.each do |impl_name, impl|
          if proto_desc['impls'].has_key?(impl_name)
            self.content << "<td class='yes'>Yes</td>"
          else
            self.content << "<td class='no'>No</td>"
          end
        end

        self.content << "</tr>"
      end

#    <td>hmac1</td>
#    <td class='no'>No</td>
#    <td class='unknown'>?</td>
#    <td class='yes'>Yes</td>
#       self.content = <<-EOS
      #self.content << "</tr>"
      self.content << "</tbody>"
      self.content << "</table>"

    end
  end

  class SSHComparisonPageGenerator < Generator
    safe true

    def generate(site)
      site.pages << SSHComparisonPage.new(site)
    end
  end

end
