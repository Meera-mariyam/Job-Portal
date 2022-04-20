from django.test import TestCase
from django.urls import reverse,resolve
from Home.models import *


class Testmodels(TestCase):
    def setUp(self) :
        Ulogin = Login(email = 'User@gmail.com',password = 'password12345',category='candidate',status = '0')
        Ulogin.save()
        User = Candidate(candidatename = 'Riya',address = 'jkajhdbcbhdghb',dob = '10-2-1996',phone = '8765432518',state = 'Kerala',
        place = 'Kochi',qualification = 'BCA',gender = 'Female',login = Ulogin,username = 'User')
        User.save()

    def test_model(self):
        record = Candidate.objects.get(id=1)
        self.assertEquals(record.candidatename,"Riya")