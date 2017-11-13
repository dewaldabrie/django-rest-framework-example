# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.core.management import call_command
from paranuara_big_brother.settings import BASE_DIR, DB
from rest_framework.test import APITestCase
from rest_framework import status

class TestCompanyAPI(APITestCase):
    """Test that the company api implements the required enpoints correctly."""

    @classmethod
    def setUpClass(cls):
        """ Load the test data"""
        call_command(
            'load_companies',
            os.path.join(BASE_DIR, 'info', 'data', 'companies.json'),
            DB,
        )

    @classmethod
    def tearDownClass(cls):
        pass

    def test_company_list(self):
        """Test that API can list companies"""
        url = '/api/company/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_string = response.content
        self.assertIn('NETBOOK', json_string)
        self.assertIn('PERMADYNE', json_string)

    def test_company_details(self):
        """Test that API can list employees in a company"""
        url = '/api/company/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_string = response.content
        self.assertIn('name', json_string)
        self.assertIn('Luna Rodgers', json_string)
        self.assertIn('Solomon Cooke', json_string)
