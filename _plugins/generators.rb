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

      # Create tables of all known protocols
      
      
      
      # Merge list of known protocols
      protocols = {
        'cipher' => {},
        'compression' => {},
        'hostkey' => {},
        'kex' => {},
        'mac' => {},
        'userauth' => {},
      }

      rfcs = site.data['rfcs']
      rfcs.each do |rfc|
        rfc['protocols'].each do |proto_class, list|
          list.each do |proto_name|
            p = protocols[proto_class].fetch(proto_name, {"rfc" => nil, "impls" => {}})
            p['rfc'] = rfc['rfc']
            protocols[proto_class][proto_name] = p
          end
        end
      end

      impls = site.data['impls']
      
      impls.each do |impl_name, impl|
        impl['protocols'].each do |proto_class, list|
          unless list.nil?
            list.each do |proto_name|
              p = protocols[proto_class].fetch(proto_name, {"rfc" => nil, "impls" => {}})
              p['impls'][impl_name] = true
              protocols[proto_class][proto_name] = p
            end
          end
        end
      end
      
      self.content = ""
      
      protocols.each do |proto_class, proto_list|
        self.content << "<h3>#{proto_class}</h3>\n"
        output_table(proto_class, proto_list, rfcs, impls)
        self.content << "<p> </p>\n"
        self.content << "<hr>\n"
      end

      self.data = {
           'layout' => 'default',
           'title' => 'The comparison',
           'generated' => true,
       }
    end
    
    def output_table(proto_class, proto_list, rfcs, impls)
      self.content << "<table class='impl-comparison'>"

      impls_sorted = impls.sort_by {|k,v| v["name"].downcase}
      protos_sorted = proto_list.sort_by {|k,v| k}

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
