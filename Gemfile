source "https://rubygems.org"

# The site is built by .github/workflows/pages.yml, not by GitHub's legacy
# Pages builder. That builder pins the github-pages gem, hence jekyll 3.10
# and Ruby Sass 3.7.4, which has neither the Sass module system nor
# color.adjust; the stylesheet needs Dart Sass.
gem "jekyll", "~> 4.4.1"

group :jekyll_plugins do
  gem "jekyll-redirect-from", "~> 0.16"
end
