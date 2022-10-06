import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APISimpleTestCase, APIClient, APIRequestFactory, force_authenticate
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ToDoViewSet
from .models import ToDo

class TestToDoViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/')
        view = ToDoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)
