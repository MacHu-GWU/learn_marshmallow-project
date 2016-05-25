#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``load_from`` 关键字可以指定在load的时候从其他的field name里load。
"""

from __future__ import print_function
from marshmallow import Schema, fields


class User(object):
    def __init__(self, name, acc, pwd):
        self.name = name
        self.acc = acc
        self.pwd = pwd


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(load_from="acc")
    password = fields.String(load_from="pwd")


schema = UserSchema()


# 虽然原数据中的项是acc, pwd, 但仍然可以从中load数据到email, password项中
user_data = {
    "name": "John David",
    "acc": "john@email.com",
    "pwd": "MyPassword",
}
result = schema.load(user_data)
print(result.data) # {'name': 'John David', 'email': 'john@email.com', 'password': 'MyPassword'}
print(result.errors) # {}

user = User(name="John David", acc="john@email.com", pwd="MyPassword")
result = schema.load(user_data)
print(result.data) # {'name': 'John David', 'email': 'john@email.com', 'password': 'MyPassword'}
print(result.errors) # {}


# load的时候依然会从默认的email, password中load数据, 优先级别是password > load_from
user_data = {
    "name": "John David",
    "email": "john@email.com",
    "password": "MyPassword",
    "pwd": "pwd",
}
result = schema.load(user_data)
print(result.data) # {'name': 'John David', 'email': 'john@email.com', 'password': 'MyPassword'}
print(result.errors) # {}