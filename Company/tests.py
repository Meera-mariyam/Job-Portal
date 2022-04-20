from django.test import TestCase,Client
from django.urls import reverse
from .models import *
import json

class Testviews(TestCase):
    def setUp(self) :
        self.client = Client()
        self.list_url = reverse('addvacancy')
        Clogin = Login(email = 'xyz@gmail.com',password = 'password12345',category='company',status = '1')
        Clogin.save()
        Vacancy = Vacancies(companyid = '001',login = Clogin(),reference_code = '002',jobtitle = 'Junior Software Engineer',
        description = 'Graduate with programming skills',keyskill = 'Python',city = 'Kochi',state = 'Kerala',pincode = '656345',
        experience = '0-2',no_opening = '2',publishedon = '4=4=2022',lastdate = '10-04-2022',joblocation = 'Kochi',contactno = '9087654534',
        qualification = 'BCA/MCA/Btecj/BE',status = '1') 
        Vacancy.save()
        
    def test_project_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'company/addvacancy.html')

   