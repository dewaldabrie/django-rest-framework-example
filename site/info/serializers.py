from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserlializers

from .models import Company, Person

class CompanySerializer(mongoserlializers.DocumentSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PersonSerializer(mongoserlializers.DocumentSerializer):
    class Meta:
        model = Company
        fields = '__all__'
