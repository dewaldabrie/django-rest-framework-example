# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.template.response import TemplateResponse
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from info.serializers import *
from info.models import *

def index(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)

class CompanyViewSet(MongoModelViewSet):

    lookup_field = 'index'
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    employees = PersonSerializer()
    # def get_queryset(selfs):
    #     return Company.objects.all()

    def retrieve(self, request, *args, **kwargs):
        index = kwargs.get('index', None)
        company = Company.objects.get(index=index)
        print(company)
        print(dir(company))
        # if len(company) != 1:
        #     raise ValueError('Company with id %s does not exist.' % index)
        queryset = Person.objects.filter(company_id=index).all()
        serializer = PersonShortSerializer(queryset, many=True, allow_empty=True)
        return Response(serializer.data)

class PersonViewSet(MongoModelViewSet):

    lookup_field = 'index'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


    def retrieve(self, request, *args, **kwargs):
        index = kwargs.get('index', None)

        # check for multiple indices (currently only two supported)
        indices = None
        if ',' in index:
            indices = index.split(',')
        else:
            return super(PersonViewSet, self).retrieve(request, *args, **kwargs)

        # return selected details for each person plus friends in
        # common with brown eyes and still alive
        queryset = Person.objects.filter(index__in=indices).all()
        serializer = CrossPersonSerializer(
            queryset,
            many=True,
            context={'indices':index}
        )
        return Response(serializer.data)
