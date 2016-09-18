#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Ref:

- http://marshmallow.readthedocs.io/en/latest/nesting.html
"""


import datetime as dt
from pprint import pprint
from marshmallow import Schema, fields
from learn_marshmallow import Base


class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None


class Blog(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author  # A User object

        from marshmallow import Schema, fields, pprint


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()


class BlogSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema)

user = User(name="Monty", email="monty@python.org")
blog = Blog(title="Something Completely Different", author=user)

#--- Test Nested ---


def test_nested():
    blog_data, errors = BlogSchema().dump(blog)
    assert blog_data["author"]["name"] == "Monty"
    assert blog_data["author"]["email"] == "monty@python.org"

if __name__ == "__main__":
    #
    test_nested()

#--- Specifying Which Fields to Nest ---


class BlogSchema2(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema, only=["email"])


class Site(Base):
    pass


class SiteSchema(Schema):
    blog = fields.Nested(BlogSchema2)


def test_specifying_which_fields_to_nest():
    schema = BlogSchema2()
    blog_data, errors = schema.dump(blog)
    assert blog_data["author"]["email"] == "monty@python.org"

    # use dot delimiters
    site = Site(blog=blog)
    schema = SiteSchema(only=['blog.author.email'])
    site_data, errors = schema.dump(site)
    assert site_data["blog"]["author"]["email"] == "monty@python.org"


if __name__ == "__main__":
    #
    test_specifying_which_fields_to_nest()

#--- Two-way Nesting ---
# ref: http://marshmallow.readthedocs.io/en/latest/nesting.html#two-way-nesting

class Author(Base):
    pass


class Book(Base):
    pass


class AuthorSchema(Schema):
    # Make sure to use the 'only' or 'exclude' params
    # to avoid infinite recursion
    books = fields.Nested('BookSchema', many=True, exclude=('author', ))

    class Meta:
        fields = ('id', 'name', 'books')


class BookSchema(Schema):
    author = fields.Nested(AuthorSchema, only=('id', 'name'))

    class Meta:
        fields = ('id', 'title', 'author')


def test_two_way_nesting():
    author = Author(id=8, name='William Faulkner')
    book = Book(id=124, title='As I Lay Dying', author=author)
    
    book_result, errors = BookSchema().dump(book)
    pprint(book_result, indent=2)

    author_result, errors = AuthorSchema().dump(author)
    pprint(author_result, indent=2)

if __name__ == "__main__":
    #
    test_two_way_nesting()
