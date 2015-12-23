#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
演示了

- 如何自定义Field。
"""

from __future__ import print_function
from marshmallow import Schema, fields, pprint
from marshmallow import validates, ValidationError
from datetime import datetime

class Credential(object):
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
    
class CredentialType(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return value.__dict__

    def _deserialize(self, value, attr, data):
        return Credential(user_id=value["user_id"], password=value["password"])

class UserSchema(Schema):
    name = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    credential = CredentialType()

if __name__ == "__main__":
    schema = UserSchema()
    
    # 原数据中"credential"项是一个Credential实例
    user = {"name": "john", "email": "john@gmail.com", 
            "created_at": datetime.now(), "credential": Credential("ec01", "7df21cb3")}
    
    # 序列化后, 变成了字典
    dump_result = schema.dump(user)
    pprint(dump_result.data)
    
    # 反序列话后, 成功恢复出Credential实例
    load_result = schema.load(dump_result.data)
    pprint(load_result.data)