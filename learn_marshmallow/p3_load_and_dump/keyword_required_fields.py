#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
我们可以指定某些项是必须要的, 不得为Null

ref: http://marshmallow.readthedocs.io/en/latest/quickstart.html?highlight=partial#required-fields
"""

from learn_marshmallow import User
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Email()

    
def test_required_fields():
    data, errors = UserSchema().load({'email': 'foo@bar.com'})
    assert errors == {'name': ['Missing data for required field.'],
        "age": ["Age is required."],
        "city": {"message": "City required", "code": 400}
    }
    
    
if __name__ == "__main__":
    #
    test_required_fields()
    