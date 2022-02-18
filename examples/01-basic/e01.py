# -*- coding: utf-8 -*-

from rich import print
from datetime import date
from marshmallow import Schema, fields


def e1_basic():
    """
    首先要理解 Marshmallow 这个框架主要是用来解决什么问题的.

    1. 允许定义一个 Schema, 这个 Schema 可以非常复杂, 无论有多少 nesting 都没问题.
        虽然在本例中没有体现出来.
    2. 对数据执行三种操作:
        - dump: 序列化, 最常用操作, 将复杂的 object, 或是 dict 序列化. 这里的
            序列化的意思是结果只由计算机可读写的几种简单数据类型和数据结构组成, 比如 str, int,
            float, bool, none, list, dict. 换言之, 被序列化后的结果还是一个 dict,
            但是可以立刻被 json.dumps 所进一步序列化. 我们可以给 dump 后的数据格式取个名字
            叫做 ``json serializable``.
        - load: 反序列化, 把之前 dump 的结果转化成原始的 object 或是 dict.
        - validation: 对 ``json serializable`` 进行数据验证. 这个步骤会在 load 的过程中
            自动执行, 而在 dump 的时候不会执行. 这里的底层逻辑是这样的:
                1. dump 的时候已经是复杂的 object 了, 应该已经被你的 application code
                    所允许, 我们理应假设这个对象是正确的, 所以不需要 validate.
                2. load 的时候是最适合做 validation 的, 因为我们可能会从不可信的数据源
                    load data.
                3. 实际工程中很常见的需求就是把复杂的对象用 json 存储. 那么我们在 load json
                    之后很可能就是把 load 出来的 dict 转化成对象, 这个步骤正是 load 和
                    validate 需要发挥作用的时候. 所以 validation 的对象主要是
                    ``json serializable``
    """
    class PersonProfileSchema(Schema):
        first_name = fields.String()
        last_name = fields.String()
        date_of_birth = fields.Date()


    schema = PersonProfileSchema()

    print(schema.dump({"first_name": "Obama", "last_name": "Barack", "date_of_birth": date(1961, 8, 4)}))
    print(schema.load({"first_name": "Obama", "last_name": "Barack", "date_of_birth": "1961-08-04"}))
    print(schema.validate({"first_name": "Obama", "last_name": "Barack", "date_of_birth": "1961-08-04"}))


if __name__ == "__main__":
    e1_basic()
    pass
