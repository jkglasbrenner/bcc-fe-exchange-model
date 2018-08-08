# -*- coding: utf-8 -*-
"""Pelican publishing settings for published content."""

from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = "https://jkglasbrenner.github.io/bcc-fe-exchange-model"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
