About marshmallow
===============================================================================
marshmallow库主要有两个功能:

1. serialize and deserialize object
2. data validation

Serialization
-------------------------------------------------------------------------------
虽然Python自带的json和pickle都可以用来做serialization, 但是json对非数字和字符串数据类型支持不良好; pickle的输出与python编译器和平台有关, 兼容性和跨平台性不够好。所以marshmallow作为补足, 可以对任意object进行序列化。并且高度可自定义的API使得用户可以定义自己的数据类型和序列化方式。


Data Validation
-------------------------------------------------------------------------------
Python社区中的Data Validation库主要有两个:

1. `marshmallow <http://marshmallow.readthedocs.org/en/latest/index.html>`_
2. `cerberus <http://docs.python-cerberus.org/en/stable/>`_

marshmallow支持对dict和object的验证。但cerberus只支持dict的验证。