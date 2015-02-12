#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yoav Ram'
SITENAME = u'Yoav Ram | Blog'
TAGLINE = "Evolution. Mathematics. Programming. Science. Lakers."
AUTHOR_BIO = "PhD Student in Tel-Aviv University"


SITEURL = 'http://blog.yoavram.com'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
THEME = "mysvbtle"
PATH = 'content'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'
LOCALE = u'he_IL'

GITHUB_URL = "https://github.com/yoavram/blog"
#GOOGLE_ANALYTICS
#DISQUS_SITENAME
TWITTER_USERNAME = "yoavram"
# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITEURL

# Blogroll
LINKS = (#('Blog', '/'),
		 ('CV', 'http://www.yoavram.com/'),
		 ('Scholar', 'http://scholar.google.com/citations?user=RIFmJvYAAAAJ'),
		 ('Twitter', 'http://twitter.com/yoavram'),
	 	  ('Github', 'http://github.com/yoavram')
	 	  #('Linkedin', 'http://www.linkedin.com/in/yoavram'),
          #('FigShare', 'http://figshare.com/authors/Yoav_Ram/99206'),
          #('OCRID', 'http://orcid.org/0000-0002-9653-4458')
        )

# Social widget
#SOCIAL = ()

DEFAULT_PAGINATION = 10

TYPOGRIFY = True
LICENSE = "CC-BY-SA 3.0"

PLUGIN_PATHS = ['..\\pelican-plugins'] #"pandoc_reader",
PLUGINS = ["pandoc_reader", "global_license", "representative_image", "share_post", "simple_footnotes"]
PANDOC_ARGS = ['--mathjax','--smart','--bibliography=blog.bib']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
