#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Darren Sholes'
SITENAME = 'Darren Sholes'
SITEURL = '.'
RELATIVE_URLS = True
LINKEDIN_URL = "https://de.linkedin.com/in/darren-sholes-5b08672a"
GITHUB_URL = "https://github.com/dsholes"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

PATH = 'content'
THEME = 'theme'
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images', 'pdfs', 'extra']
DIRECT_TEMPLATES = ['index', 'tags', 'sitemap','archives']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# For "Notebook" page, Use the tags.html as the template
# TAGS_URL = 'notebook/'
# TAGS_SAVE_AS = 'notebook/index.html'
ARTICLE_URL = 'notebook/{slug}'
ARTICLE_SAVE_AS = 'notebook/{slug}/index.html'
ARCHIVES_URL = 'notebook/'
ARCHIVES_SAVE_AS = 'notebook/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DEFAULT_PAGINATION = 3
DEFAULT_ORPHANS = 0
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
PAGINATED_TEMPLATES = {'tags': None}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'use_pygments': 'false',
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'marker': '[TableOfContents]',
            'title': 'Table of Contents',
            'anchorlink': False,
            'permalink': False,
            'baselevel': 1,
        },
    },
    'output_format': 'html5',
}

PLUGIN_PATHS=["plugins"]
PLUGINS = ["render_math","summary","neighbors"]
SUMMARY_USE_FIRST_PARAGRAPH = True
MATH_JAX = {
    "mathjax_font": 'sansserif',
}

DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
