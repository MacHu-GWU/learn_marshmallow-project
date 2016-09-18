#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pre_load阶段是指将原始数据在load之前的预处理阶段。常用来做数据预处理。
"""

from marshmallow import Schema, fields, pre_load


def namelize(name):
    chunks = [s.strip() for s in name.split(" ") if s.strip()]
    chunks = [s[0].upper() + s[1:].lower() for s in chunks]
    return " ".join(chunks)


def test_namify():
    assert namelize(" john    DAVID ") == "John David"


class NewsSchema(Schema):
    title = fields.String()
    author = fields.String()

    @pre_load
    def namelize_title(self, in_data):
        in_data["title"] = namelize(in_data["title"])
        return in_data

    @pre_load
    def namelize_author(self, in_data):
        in_data["author"] = namelize(in_data["author"])
        return in_data


def test_pre_load():
    news_data = {"title": "a new marshmallow is released!",
                 "author": " john david "}
    news = NewsSchema().load(news_data).data
    assert news["title"] == "A New Marshmallow Is Released!"
    assert news["author"] == "John David"


if __name__ == "__main__":
    #
    test_namify()
    test_pre_load()
