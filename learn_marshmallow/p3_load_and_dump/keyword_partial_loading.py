#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
缺少定义了required关键字的field会抛出异常。而有时候我们希望只load部分项, 那么
我们可以用partial关键字来指定我们要load哪些。

ref: http://marshmallow.readthedocs.io/en/latest/quickstart.html?highlight=partial#partial-loading
"""

from learn_marshmallow import User
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    
    
def test_partial_loading():
    data, errors = UserSchema().load({"age": 42}, partial=("name",))
    # OR UserSchema(partial=("name",)).load({"age": 42})
    data, errors  # => ({"age": 42}, {})
    assert data == {"age": 42}
    assert errors == {}
    
    
if __name__ == "__main__":
    #
    test_partial_loading()
    