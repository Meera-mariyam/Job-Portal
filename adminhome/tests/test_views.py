from django.test import TestCase,Client
from django.urls import reverse
from adminhome.models import *
import json

class Testviews(TestCase):
    def test_Project_Get(self):
        client = Client()

        response = client.get(reverse('allcompany'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'adminhome/allcompany.html')
