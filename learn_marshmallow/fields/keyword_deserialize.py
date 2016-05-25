#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Method和Function项都支持deserialize关键字, 可以定制load的行为。
"""

from __future__ import print_function
from marshmallow import Schema, fields


class UserSchema(Schema):
    # `Method` takes a method name (str), Function takes a callable
    balance = fields.Method("get_balance", deserialize="load_balance")
        
    def get_balance(self, obj):
        return obj.income - obj.debt

    def load_balance(self, value):
        return float(value)


schema = UserSchema()
result = schema.load({"balance": "100.00"})
print(result.data)


class UserSchema(Schema):
    # `Method` takes a method name (str), Function takes a callable
    balance = fields.Function(lambda obj: obj.income - obj.debt, 
                              deserialize=lambda value: float(value))

schema = UserSchema()
result = schema.load({"balance": "100.00"})
print(result.data)