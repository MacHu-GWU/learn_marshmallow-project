#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Method项会在dump的时候, 生成一个新的项。和Function不同的是, 该方法只接受以obj为
输入。在load的时候不进行计算。(load的时候的计算逻辑应当在Application Class里定义)
"""

from __future__ import print_function
from datetime import datetime
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    
    # 定义一个 method field
    days_from_2016 = fields.Method("get_days_since_created")

    def get_days_since_created(self, obj):
        return int((datetime.now() - obj["created_at"]).total_seconds() // 86400)

schema = UserSchema()

user_data = {
    "name": "John David",
    "email": "john@email.com",
    "created_at": "2016-01-01",
}
result = schema.load(user_data)
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
assert result.data == {
    'name': 'John David',
    'email': 'john@email.com',
    'created_at': '2016-01-01T00:00:00+00:00',
    'days_from_2016': 213,
}
