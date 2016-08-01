#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**validation只发生在load的时刻**, dump的时候是不进行数据验证的。
"""

from __future__ import print_function
from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class UserSchema(Schema):
    favorite_number = fields.Int()
    
    @validates("favorite_number")
    def validate_favorite_number(self, value):
        if value not in range(10): # if not in 0 ~ 9
            raise ValidationError("favorite number has to be from 0 ～ 9")
        
schema = UserSchema()

user_data = {"favorite_number": 99}
result = schema.dump(user_data)
assert result.data == {"favorite_number": 99}
assert result.errors == {} # no error

result = schema.load(user_data)
assert result.data == {"favorite_number": 99}
assert result.errors == {'favorite_number': ['favorite number has to be from 0 ～ 9']} # has error