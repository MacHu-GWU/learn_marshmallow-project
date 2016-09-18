#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
field level validation是指在分别独立地读取每一项的值时进行的数据验证。也就是只
考虑field value的值, 而不考虑和其他field或整体之间的关系。

validation **只在load的时候发生** (dump的时候从逻辑上讲, 不需要)。

field level validation有两种实现方法:

1. 在定义field时定义validate关键字为validate函数。
2. 使用validates装饰器定义一个方法。
"""

import string

from learn_marshmallow import User
from marshmallow import Schema, fields, validates, ValidationError
from datetime import datetime, date

alphadigits = string.ascii_letters + string.digits


def validate_password(password):
    if len(set(r"!@#$%^&*()_-+=~`[{]}|\:;<,>.?/").intersection(password)) == 0:
        raise ValidationError("Has to have at lease one special character.")
    if " " in password:
        raise ValidationError("Can not has empty space.")
    if len(set(string.ascii_uppercase).intersection(password)) == 0:
        raise ValidationError("Has to have at lease one uppercase.")
    if len(set(string.digits).intersection(password)) == 0:
        raise ValidationError("Has to have at lease one digits.")


class UserSchema(Schema):
    # 方法1, 定义lambda函数
    nickname = fields.String(
        validate=lambda v: len(set(v).difference(alphadigits)) == 0)
    # 方法1, 定义validate函数
    password = fields.String(validate=validate_password)
    dob = fields.Date()
    
    # 方法2, 使用装饰器定义validate函数
    @validates("dob")
    def validate_dob(self, value):
        if date(value.year + 18, value.month, value.day) > date.today():
            raise ValidationError("your age is not 18 and over.")


def test_validate():
    user_data = {"nickname": "good boy",
                 "password": "mypassword",
                 "dob": "2003-01-01"}

    result = UserSchema().load(user_data)
    assert result.data == {}
    assert result.errors == {
        'nickname': ['Invalid value.'],
        'password': ['Has to have at lease one special character.'],
        'dob': ['your age is not 18 and over.'],
    }


if __name__ == "__main__":
    test_validate()
