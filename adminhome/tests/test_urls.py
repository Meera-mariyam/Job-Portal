from django.test import SimpleTestCase
from django.urls import reverse,resolve
from adminhome.views import *


class Testurls(SimpleTestCase):
    def test_url_is_resolved(self):
        url = reverse('Adminhomee')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,Adminhomee)

    def test_url_is_resolvs(self):
        url = reverse('acceptcompany',args = ['1'])
        self.assertEquals(resolve(url).func.view_class,Acceptcompany)
