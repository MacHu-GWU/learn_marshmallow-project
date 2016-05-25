#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import datetime
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    uppername = fields.Function(lambda obj: obj["name"].upper())
    
schema = UserSchema()

user = {
    "name": "John David",
    "email": "john@email.com",
    "created_at": "2016-01-01",
}
result = schema.load(user)
print(result.data)


user_data = {
    "name": "John David",
    "email": "john@email.com",
    "created_at": datetime(2016, 1, 1),
}
result = schema.dump(user_data)
print(result.data)