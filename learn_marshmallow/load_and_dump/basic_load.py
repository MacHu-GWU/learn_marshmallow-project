#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

from __future__ import print_function
from marshmallow import Schema, fields, post_load


class User(object):

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()

    @post_load
    def make_user(self, data):
        return User(**data)

user_schema = UserSchema()
user_data = {'name': 'David', 'email': 'david@email.com'}
result = user_schema.load(user_data)
assert isinstance(result.data, User)
assert result.data.name == "David"
assert result.data.email == "david@email.com"
