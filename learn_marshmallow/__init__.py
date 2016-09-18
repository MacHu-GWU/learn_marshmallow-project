#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__short_description = ("Learn marshmallow, universe data valdiation light orm"
                       "framework")
__license__ = "MIT"
__author__ = "Sanhe Hu"


class Base(object):
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)
            
    def __repr__(self):
        kwargs = list()
        for attr, value in self.__dict__.items():
            kwargs.append("%s=%r" % (attr, value))
        return "%s(%s)" % (self.__class__.__name__, ", ".join(kwargs))
    
class User(Base):
    pass