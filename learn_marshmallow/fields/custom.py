#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自定义Field。自定义Field主要要实现三个方法:

- Field._validate: 在load的时候对值进行验证
- Field._serialize: 支持dump方法
- Field._deserialize: 支持load方法
"""

from six import string_types
from marshmallow import Schema, fields, ValidationError


class NameTitleFormatted(fields.Field):

    """每一个单词的第一个字母大写。
    """

    def _validate(self, value):
        """"when can  I  see  you  again " -> "When Can I See You Again"
        """
        if isinstance(value, string_types):
            value = value.strip()
            if value:
                chunks = list()
                for s in [s.strip() for s in value.split(" ") if s.strip()]:
                    if str.isalpha(s):
                        s = s[0].upper() + s[1:].lower()
                        chunks.append(s)
                return " ".join(chunks)
            else:
                raise ValidationError("Can't be empty string")
        else:
            raise ValidationError("Not a string type")

    def _serialize(self, value, attr, obj):
        return self._validate(value)

    def _deserialize(self, value, attr, data):
        return self._validate(value)


class Music(object):

    def __init__(self, title, artists):
        self.title = title
        self.artists = artists


class MusicSchema(Schema):
    title = NameTitleFormatted()
    artists = fields.List(NameTitleFormatted())


schema = MusicSchema()


music_data = {
    "title": "when   can   i   see   you   again",
    "artists": ["owl city", ],
}
result = schema.load(music_data)
assert result.data == {
    'title': 'When Can I See You Again', 'artists': ['Owl City']}
assert result.errors == {}

music_data = {
    "title": "   ",
    "artists": "owl city",
}
result = schema.load(music_data)
assert result.data == {}
assert result.errors == {
    'title': ["Can't be empty string"], 'artists': ['Not a valid list.']}
