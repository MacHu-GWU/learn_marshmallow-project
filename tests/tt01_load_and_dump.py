#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
演示了：

- 如何对数据进行序列化和反序列化。
- 如何自定义validator的行为。
"""

from __future__ import print_function
from marshmallow import Schema, fields, post_load, pprint
from marshmallow import validates, ValidationError
from datetime import datetime

class User(object):
    def __init__(self, name, email, favorite_number=7, **kwargs):
        self.name = name
        self.email = email
        self.favorite_number = favorite_number
        self.created_at = datetime.now()
        
        # 由于在UserSchema.make_user方法中, data是包含created_at项的
        # 而User.__init__方法中默认是不包含这一项的。这样会导致
        # UserSchema.make_user(**data)方法出错。为了能够从dump后的数据中
        # 重新恢复完整的User对象, 我们需要在User.__init__方法中定义**kwargs
        # 可选参数, 然后将可选参数赋值到对应的属性上。
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
            
    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
    
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    favorite_number = fields.Integer()
    created_at = fields.DateTime()
    
    @post_load
    def make_user(self, data):
        return User(**data)
    
    @validates("favorite_number")
    def validate_quantity(self, value):
        """marshmallow可以使用 @validates 装饰器来定义自定义的field validator。
        而 ValidationError 可以被用来生成数据验证异常。
        
        ref: http://marshmallow.readthedocs.org/en/latest/quickstart.html#field-validators-as-methods
        """
        if value not in range(10):
            raise ValidationError("favorite_number has to be 0 to 9")    
    
if __name__ == "__main__":
    import time
    
    def example_dump_and_load():
        schema = UserSchema()
        
        user = User(name="Monty", email="monty@python.org")
        dump_result = schema.dump(user)
        json_result = schema.dumps(user)
        print(dump_result.data) # dict type
        print(json_result.data) # str type
        
        time.sleep(0.001)
        
        load_result = schema.load(dump_result.data)
        user_loaded = load_result.data
        
        print(user.name == user_loaded.name) # True
        print(user.email == user_loaded.email) # True
        print(user.created_at.microsecond == user_loaded.created_at.microsecond) # True
        
#     example_dump_and_load()
    
    def example_validation():
        """本例演示了如何使用marshmallow来进行data validation。
        
        在 ``Schema.load`` 方法所返回的 ``UnmarshalResult`` 中, 我们可以使用 ``.error``
        来访问错误信息。
        """
        schema = UserSchema()
        load_result = schema.load({"email": "foo"})
        
        print(load_result.data) # {} 由于没有成功, 所有没有数据
        print(load_result.errors) # {'email': ['Not a valid email address.']}
        
#     example_validation()

    def example_customize_validation():
        """本例演示了如何使用自定义的validator来验证某些Field。
        
        注意: 本例中partial关键字可以忽略其他缺失的项。
        ref: http://marshmallow.readthedocs.org/en/latest/quickstart.html#partial-loading
        """
        schema = UserSchema()
        load_result = schema.load({"favorite_number": 10}, partial=True)
        
        print(load_result.data) # {'favorite_number': 10}
        print(load_result.errors) # {'favorite_number': ['favorite_number has to be 0 to 9']}
        
#     example_customize_validation()