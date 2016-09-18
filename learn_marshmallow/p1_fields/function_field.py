#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
function field是指在dump的时候, 能生成一个field, 由自定义的function计算而来。
"""

from __future__ import print_function
from datetime import datetime
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    # 定义一个 function field
    uppername = fields.Function(lambda obj: obj["name"].upper())

schema = UserSchema()

user = {
    "name": "John David",
    "email": "john@email.com",
    "created_at": "2016-01-01",
}
result = schema.load(user)
assert result.data == {
    'name': 'John David',
    'email': 'john@email.com',
    'created_at': datetime(2016, 1, 1, 0, 0),
}


user_data = {
    "name": "John David",
    "email": "john@email.com",
    "created_at": datetime(2016, 1, 1),
}
result = schema.dump(user_data)
assert result.data["uppername"] == "JOHN DAVID"
