#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
普通的Validation只是对每一个field的值本身进行验证, 并不考虑和其他field之间的
关系。而Schema Level Validation是从全局角度出发, 考虑所有的数据关系。
"""

from __future__ import print_function
from marshmallow import Schema, fields, validates_schema, ValidationError


class NumberSchema(Schema):
    field_a = fields.Integer()
    field_b = fields.Integer()

    @validates_schema
    def validate_numbers(self, data):
        if data['field_b'] >= data['field_a']:
            raise ValidationError('field_a must be greater than field_b')


schema = NumberSchema()
result = schema.load({'field_a': 1, 'field_b': 2})
print(result.data)
print(result.errors) # {'_schema': ['field_a must be greater than field_b']}