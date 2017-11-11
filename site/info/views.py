# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from info.serializers import *
from info.models import *

def index(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)

class CompanyViewSet(MongoModelViewSet):

    lookup_field = 'index'
    serializer_class = CompanySerializer

    def get_queryset(selfs):
        return Company.objects.all()


class PersonViewSet(MongoModelViewSet):

    lookup_field = 'guid'
    serializer_class = PersonSerializer

    def get_queryset(selfs):
        return Person.objects.all()

