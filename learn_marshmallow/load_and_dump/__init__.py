#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在各种App的数据交换层, 我们有这样三个概念:

1. 符合Schema的Application-Level Data Structure, 可以是类, 可以是结构化的字典数据。
2. 用于数据交换的数据结构, 比如Json, Pickle序列。
3. 处于中间一层, 可能是其他模块的输出, 也可能是用户的输入。

- dump/serialize: 将 ``1`` 或 ``3`` 转化为 ``2``  
- load/deserialize: 将 ``2`` 或 ``3`` 转化为 ``1``

marshmallow的主要功能是就是解决这之间的转化, 数据验证等问题。

在我们的实际应用中, 比较大的需求是将各种不符合Schema标准的数据, 也就是 ``3`` 或 ``2``
转化成我们的应用所使用的 ``1``, 即loading。
"""