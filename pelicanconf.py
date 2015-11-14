#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DyND Developers'
SITENAME = u'DyND Multi-Dimensional Array Library'
SITEURL = 'http://libdynd.org/'

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

PLUGINS = ["page_hierarchy", "ipynb"]

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/{slug}.html'
SLUGIFY_SOURCE = 'basename'

STATIC_PATHS = ['CNAME', 'favicon.ico', 'images']
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

