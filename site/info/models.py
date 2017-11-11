# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import Document, EmbeddedDocument, fields
from django.db import models

# Create your models here.
class Company(Document):
    index = fields.IntField()
    name = fields.StringField()


class Person(Document):
    _id = fields.StringField()
    index = fields.IntField()
    guid = fields.UUIDField()
    has_died = fields.BooleanField()
    balance = fields.StringField()
    picture = fields.URLField()
    age = fields.IntField()
    eyeColor = fields.StringField()
    name = fields.StringField
    gender = fields.StringField
    company_id = fields.IntField()
    email = fields.EmailField()
    phone = fields.StringField()
    address = fields.MultiLineStringField()
    about = fields.MultiLineStringField()
    registered = fields.DateTimeField()
    tags = fields.ListField()
    friends = fields.DictField()
    greeting = fields.MultiLineStringField()
    favourite_food = fields.ListField() # this field will require splitting into fruit and vegetables
    favourite_fruits = fields.ListField()
    favourite_vegetables = fields.ListField()

    KNOWN_FRUITS = ['apple', 'orange', 'banana', 'strawberry', 'cucumber']
    KNOWN_VEGGIES = ['beetroot', 'carrot', 'celery']

    def split_foods_into_fruits_and_vegetables(self, foods):
        """
        Take a list of foods and split into a list of fruits and a list of veggies.
        :param foods: list of foods
        :return: tuple containing list of ruits first, then veggies
        """
        fruits = [f for f in foods if f in self.KNOWN_FRUITS]
        veggies = [f for f in foods if f in self.KNOWN_VEGGIES]

        return (fruits, veggies)