#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``attribute`` 关键字可以使得在dump的时候, 从原数据里attribute所声明的field中dump
到Schema所定义的关键字的项中。
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
    email = fields.Email(attribute="acc")
    password = fields.String(attribute="pwd")


schema = UserSchema()


# 虽然原数据中的项是acc, pwd, 但是依旧会被dump到email, password项中
user_data = {
    "name": "John David",
    "acc": "john@email.com",
    "pwd": "MyPassword",
}
result = schema.dump(user_data)
assert result.data == {
    'name': 'John David', 'email': 'john@email.com', 'password': 'MyPassword'}
assert result.errors == {}

user = User(name="John David", acc="john@email.com", pwd="MyPassword")
result = schema.dump(user)
assert result.data == {
    'name': 'John David', 'email': 'john@email.com', 'password': 'MyPassword'}
assert result.errors == {}


# 原数据中的项是email, password, 但是dump的时候并不认
user_data = {
    "name": "John David",
    "email": "john@email.com",
    "password": "MyPassword",
}
result = schema.dump(user_data)
assert result.data == {'name': 'John David'}
assert result.errors == {}
