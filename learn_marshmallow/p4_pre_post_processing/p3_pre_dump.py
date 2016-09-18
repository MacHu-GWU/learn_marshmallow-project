#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pre_dump是将实例dump成数据之前的阶段。
"""

from marshmallow import Schema, fields, pre_dump
from learn_marshmallow import User


def get_initial(name):
    chunks = [chunk.strip()[0].upper()
              for chunk in name.split(" ") if chunk.strip()]
    return "".join(chunks)


def test_get_initial():
    assert get_initial("John David") == "JD"


class UserSchema(Schema):
    name = fields.String()

    @pre_dump
    def initialize_name(self, user):
        user.name = get_initial(user.name)
        return user


def test_pre_dump():
    user = User(name="John David")
    user_data = UserSchema().dump(user).data
    assert user_data == {"name": "JD"}

if __name__ == "__main__":
    test_get_initial()
    test_pre_dump()
