Title: Getting Started With Pelican
Date: 2019-01-03
image_url: images/pelican.jpg
tags: pelican, python

Hey There. I'm just writing a simple code test:

What happens with `inline` code?
<!-- PELICAN_END_SUMMARY -->

```python
from __future__ import print_function, unicode_literals

import functools
import logging
import os
from collections import namedtuple
from math import ceil

import six

logger = logging.getLogger(__name__)
PaginationRule = namedtuple(
    'PaginationRule',
    'min_page URL SAVE_AS',
)


class Paginator(object):
    def __init__(self, name, url, object_list, settings, per_page=None):
        self.name = name
        self.url = url
        self.object_list = object_list
        self.settings = settings
        if per_page:
            self.per_page = per_page
            self.orphans = settings['DEFAULT_ORPHANS']
        else:
            self.per_page = len(object_list)
            self.orphans = 0

        self._num_pages = self._count = None

    def page(self, number):
        "Returns a Page object for the given 1-based page number."
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return Page(self.name, self.url, self.object_list[bottom:top], number,
                    self, self.settings)
```
