from http import client
from urllib import response
import django
from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from Home.models import *
import json

class TestViews(TestCase):

    def setUp(self) :
        self.client = Client()
        self.list_url = reverse('candreg')
        Ulogin = Login(email = 'User@gmail.com',password = 'password12345',category='candidate',status = '0')
        Ulogin.save()
        User = Candidate(candidatename = 'Riya',address = 'jkajhdbcbhdghb',dob = '10-2-1996',phone = '8765432518',state = 'Kerala',
        place = 'Kochi',qualification = 'BCA',gender = 'Female',email=Ulogin.email,login = Ulogin,username = 'User')
        User.save()
        

    def test_Project_Get(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Home/candidate_reg.html')

    def test_project_Post(self):
        response = self.client.post(self.list_url,data={
        'candidatename':self.candidatename ,
        'addr' :self.address ,
        'dob'   :self.dob, 
        'phone':self.phone, 
        'state' :self.state, 
        'place' :self.place ,
        'qualification':self.qualification ,
        'gender':self.gender ,
        'login':self.login ,
        'username' :self.username ,
        'email' : self.email ,
        'category':self.category,
        'password':self.password 
        })
        self.assertEqual(response.status_code,302)
        users = get_user_model().objects.all()
        #record = Candidate.objects.create()
        #record1 = Candidate.objects.get(id=1)
        self.assertEquals(users.count(),1)
