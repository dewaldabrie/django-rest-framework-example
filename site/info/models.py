# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import Document, EmbeddedDocument, fields
from django.db import models

# Create your models here.
class Company(Document):
    index = fields.IntField(unique=True)
    name = fields.StringField(unique=True)


class Person(Document):
    _id = fields.StringField()
    index = fields.IntField(unique=True)
    guid = fields.UUIDField(unique=True)
    has_died = fields.BooleanField()
    balance = fields.FloatField()
    picture = fields.URLField()
    age = fields.IntField()
    eyeColor = fields.StringField()
    name = fields.StringField()
    gender = fields.StringField()
    company_id = fields.IntField()
    email = fields.EmailField(unique=True)
    phone = fields.StringField()
    address = fields.MultiLineStringField()
    about = fields.MultiLineStringField()
    registered = fields.DateTimeField()
    tags = fields.ListField(fields.StringField())
    friends = fields.ListField(fields.DictField())
    greeting = fields.MultiLineStringField()
    favouriteFood = fields.ListField(fields.StringField()) # this field will require splitting into fruit and vegetables
    favouriteFruits = fields.ListField(fields.StringField())
    favouriteVegetables = fields.ListField(fields.StringField())

    KNOWN_FRUITS = ['apple', 'orange', 'banana', 'strawberry', 'cucumber']
    KNOWN_VEGGIES = ['beetroot', 'carrot', 'celery']

    @staticmethod
    def split_foods_into_fruits_and_vegetables(foods):
        """
        Take a list of foods and split into a list of fruits and a list of veggies.
        :param foods: list of foods
        :return: tuple containing list of ruits first, then veggies
        """
        fruits = [f for f in foods if f in Person.KNOWN_FRUITS]
        veggies = [f for f in foods if f in Person.KNOWN_VEGGIES]

        return (fruits, veggies)