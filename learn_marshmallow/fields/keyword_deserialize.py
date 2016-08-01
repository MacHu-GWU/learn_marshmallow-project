#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Method和Function项都支持deserialize关键字, 可以定制load的行为。
"""

from __future__ import print_function
from marshmallow import Schema, fields


class User(object):

    def __init__(self, name, income, debt):
        self.name = name
        self.income = income
        self.debt = debt


class UserSchema(Schema):
    # `Method` takes a method name (str), Function takes a callable
    balance = fields.Method("get_balance", deserialize="load_balance")

    def get_balance(self, obj):
        return obj.income - obj.debt

    def load_balance(self, value):
        """will be called in ``schema.load(data)``
        """
        return float(value)


schema = UserSchema()
result = schema.load({"balance": "100.00"})
assert result.data == {"balance": 100.0}

user = User("John", 100000, 30000)
result = schema.dump(user)
assert result.data == {"balance": 70000}


class UserSchema(Schema):
    # `Method` takes a method name (str), Function takes a callable
    balance = fields.Function(lambda obj: obj.income - obj.debt,
                              deserialize=lambda value: float(value))

schema = UserSchema()
result = schema.load({"balance": "100.00"})
assert result.data == {"balance": 100.0}
