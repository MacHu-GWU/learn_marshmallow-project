#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import pytest
from marshmallow import Schema, fields, ValidationError


class User(object):

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()


def test_basic():
    """marshmallow最可以对对象的实例，或是字典数据进行序列化操作。

    dump的结果返回的是MarshalResult类。有两个属性data和errors。
    其中data储存了序列化后的数据, errors储存了序列化后的错误信息。
    """
    user_schema = UserSchema()

    user = User(name="David", email="david@email.com")
    result = user_schema.dump(user)
    assert result.data == {'name': 'David', 'email': 'david@email.com'}

    user_data = {"name": "David", "email": "david@email.com"}
    result = user_schema.dump(user_data)
    assert result.data == {'name': 'David', 'email': 'david@email.com'}

# test_basic()


def test_error():
    """当某些项出现错误时，该项则不会被序列化，而错误会被储存在errors这一
    属性中。最终只会返回已被成功序列化的项目。该过程并不会抛出异常，如果你
    需要在出现错误时抛出异常，则需要使用strict模式。做法是在生成schema实例
    时候加入 ``strict=True`` 关键字。

    验证错误的规则是由validator函数定义的，这一部分将在别的章节中介绍。
    """
    user_schema = UserSchema()

    user = User(name="David", email="John")
    result = user_schema.dump(user)
    assert result.data == {'name': 'David'} # 错误项不会被序列化
    assert result.errors == {'email': ['Not a valid email address.']}

    user_schema = UserSchema(strict=True)
    with pytest.raises(ValidationError):
        result = user_schema.dump(user)  # a ValidationError will be raised

# test_error()


def test_missing_undefined_field():
    """如果对象缺失了某些项目，或是多了某些Schema中没有被定义的项，Schema会
    尽量只序列化已被定义的项。

    marshmallow无法限制在dump的时候，对象必须要有某些项目，也无法限制对象不能有
    Schema中未定义的项。而这两个功能在load的时候可以实现。
    """
    user_schema = UserSchema(strict=True)
    user = User(name="David", password="MyPassword")
    result = user_schema.dump(user)
    assert result.data == {'name': 'David'}
    assert result.errors == {}

# test_missing_undefined_field()


def test_only():
    """创建schema实例的时候，可以用only关键字限定只对一部分项进行序列化。
    """
    user_schema = UserSchema(only=("name",))
    user = User(name="David", email="david@email.com")
    result = user_schema.dump(user)
    assert result.data == {'name': 'David'}
    assert result.errors == {} #无错误

# test_only()
