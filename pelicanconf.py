# -*- coding: utf-8 -*-
"""Pelican setings for BCC Fe exchange model Jupyter notebook."""

from __future__ import unicode_literals

# GENERAL
AUTHOR = "James K. Glasbrenner"
SITENAME = "BCC Fe exchange model"
SITEURL = ""
SLACK_URL = ""
GITHUB_URL = "https://github.com/jkglasbrenner/bcc-fe-exchange-model/"
UNIVERSITYURL = ""
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# PROCESSING
CACHE_CONTENT = False
READERS = {
    "html": None,
    "yaml": None,
}

# THEME
THEME = "src/theme"
THEME_STATIC_PATHS = [
    "assets",
]
TYPOGRIFY = True
HIGHLIGHT_JS_STYLE = "default"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Define paths and urls
PATH = "docs"
IMAGES_PATH = "img"
STATIC_PATHS = [
    IMAGES_PATH,
    "data",
]
PAGE_PATHS = ["page"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = ""
ARTICLE_SAVE_AS = ""
AUTHOR_URL = ""
AUTHOR_SAVE_AS = ""
DRAFT_URL = ""
DRAFT_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
TAG_URL = ""
TAG_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""
INDEX_SAVE_AS = "index.html"
DIRECT_TEMPLATES = []
PAGINATED_DIRECT_TEMPLATES = []
TEMPLATE_PAGES = {}
SUMMARY_MAX_LENGTH = 50

# Menu items
MENUITEMS = []

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pandoc_reader",
    "ipynb.markup",
]

# Plugin: ipynb
MARKUP = ("md", "ipynb")
IPYNB_USE_METACELL = False
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False
IPYNB_PREPROCESSORS = []
IPYNB_EXPORT_TEMPLATE = THEME + "/templates/ipynb/page.tpl"
IPYNB_STOP_SUMMARY_TAGS = [
    ('div', ('class', 'input')),
    ('div', ('class', 'output')),
    ('h2', ('id', 'Header-2')),
]
IPYNB_GENERATE_SUMMARY = False
IPYNB_EXTEND_STOP_SUMMARY_TAGS = []
IPYNB_NB_SAVE_AS = ""
IGNORE_FILES = [
    ".ipynb_checkpoints",
]

# Plugin: Custom Article URLs
CUSTOM_ARTICLE_URLS = {}

# Plugin: Pandoc Reader
PANDOC_ARGS = [
    "--no-highlight",
    "--filter",
    "pandoc-citeproc",
    "--mathjax",
    "--variable",
    "\"mathjax-url:#\"",
]
PANDOC_EXTENSIONS = [
    "+autolink_bare_uris",
    "+ascii_identifiers",
    "-tex_math_single_backslash",
    "-implicit_figures",
    "+multiline_tables",
    "+tex_math_double_backslash",
    "+smart",
]
