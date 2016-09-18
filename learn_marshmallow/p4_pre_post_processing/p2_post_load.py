#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
post_load是指将原始数据在load成了data之后的阶段, 常用于将load成功之后的数据转化
成实例。
"""

from marshmallow import Schema, fields, post_load
from learn_marshmallow import User


class UserSchema(Schema):
    name = fields.String()

    @post_load
    def make_user(self, data):
        return User(**data)


def test_post_load():
    user_data = {"name": "John"}
    user = UserSchema().load(user_data).data
    assert user.name == "John"


if __name__ == "__main__":
    #
    test_post_load()
