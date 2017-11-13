from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserlializers

from .models import Company, Person

class CompanySerializer(mongoserlializers.DocumentSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PersonSerializer(mongoserlializers.DocumentSerializer):
    username = mongoserlializers.serializers.CharField(source='name')
    fruits = mongoserlializers.serializers.CharField(source='favouriteFruits')
    vegetables = mongoserlializers.serializers.CharField(source='favouriteVegetables')

    class Meta:
        model = Person
        fields = ('username', 'age', 'fruits', 'vegetables')


class PersonShortSerializer(mongoserlializers.DocumentSerializer):
    class Meta:
        model = Person
        fields = ('name',)


class CrossPersonSerializer(mongoserlializers.DocumentSerializer):
    friends_in_common = mongoserlializers.serializers.SerializerMethodField()

    def get_friends_in_common(self, instance):
        # split indices
        indices = map(int, self.context.get('indices').split(','))
        this_index = instance.index
        other_index = list(set(indices) - set([this_index]))[0]
        # find set of mutual friends
        this_friends = set([d['index'] for d in instance.friends])
        other_friends = set([d['index'] for d in Person.objects.get(index=other_index).friends])
        mutual_friends = list(this_friends.intersection(other_friends))
        # filter on brown eyes and still alive
        specific_mutual_friends = Person.objects.filter(
            has_died=False,
            eyeColor='brown',
            index__in=mutual_friends,
        ).all()
        # use short serializer to only show the friends' names
        return PersonShortSerializer(specific_mutual_friends, many=True).data

    class Meta:
        model = Person
        fields = ('name', 'age', 'address', 'phone', 'friends_in_common')
