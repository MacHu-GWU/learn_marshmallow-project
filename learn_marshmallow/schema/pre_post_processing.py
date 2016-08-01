#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请注意pre_load, pre_dump, post_load, post_dump是Schema级的, 不是field级的。

Ref:

- http://marshmallow.readthedocs.io/en/latest/extending.html?highlight=pre_load#pre-processing-and-post-processing-methods
"""

from __future__ import print_function
from marshmallow import Schema, fields, pre_load, pre_dump