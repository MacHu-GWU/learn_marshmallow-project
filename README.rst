Learn marshmallow
===============================================================================
在Python社区中的Data Validation库主要有两个:

1. `marshmallow <http://marshmallow.readthedocs.org/en/latest/index.html>`_
2. `cerberus <http://docs.python-cerberus.org/en/stable/>`_

marshmallow是一个功能强大的 ``Data Serialize`` 和 ``Data Validation`` 框架, 可以在不修改类定义的代码的情况下进行高度定制。并且扩展性非常强大。支持dict和对象之间的load, dump, validation。而cerberus主要是面对字典数据的data validation。所以marshmallow更加通用, 而cerberus更加轻量, 对dict类型的数据支持的更好。