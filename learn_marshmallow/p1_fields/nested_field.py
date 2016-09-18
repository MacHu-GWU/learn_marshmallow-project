#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
marshmallow支持nested field, 也就是说某个field对应着一个schema。
"""

from marshmallow import fields, Schema, post_load
from sfm import nameddict


class Profile(nameddict.Base):

    def __init__(self, name, email):
        self.name = name
        self.email = email


class ProfileSchema(Schema):
    name = fields.String()
    email = fields.Email()

    @post_load
    def make_profile(self, data):
        return Profile(**data)


class User(nameddict.Base):

    def __init__(self, _id, profile):
        self._id = _id
        self.profile = profile


class UserSchema(Schema):
    _id = fields.Integer()
    profile = fields.Nested(ProfileSchema)

    @post_load
    def make_user(self, data):
        return User(**data)


def test_nested_field():
    user_schema = UserSchema()
    user_data = {
        "_id": 1,
        "profile": {
            "name": "John",
            "email": "john@example.com",
        }
    }
    user = user_schema.load(user_data).data
    assert user._id == 1
    assert user.profile.name == "John"
    assert user.profile.email == "john@example.com"


if __name__ == "__main__":
    #
    test_nested_field()
