#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``dump_to`` 关键字可以使得在dump的时候, 从原数据里Schema所定义的项中, dump到
dump_to所声明的field中。
"""

from __future__ import print_function
from marshmallow import Schema, fields


class User(object):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(dump_to="acc")
    password = fields.String(dump_to="pwd")


schema = UserSchema()

user_data = {
    "name": "John David",
    "email": "john@email.com",
    "password": "MyPassword",
}
result = schema.dump(user_data)
print(result.data) # {'name': 'John David', 'acc': 'john@email.com', 'pwd': 'MyPassword'}
print(result.errors) # {}

user = User(name="John David", email="john@email.com", password="MyPassword")
result = schema.dump(user)
print(result.data) # {'name': 'John David', 'acc': 'john@email.com', 'pwd': 'MyPassword'}
print(result.errors) # {}