from django.db import models
from Home.models import Login
from Company.models import Vacancies

class ApplyVacancy(models.Model):
    vacancyid = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    candidatename = models.CharField(max_length=100)
    candidatemail = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    keyskill = models.CharField(max_length=800)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume')
    candlogin = models.ForeignKey(Login, on_delete=models.CASCADE)
    applystatus = models.IntegerField(default=0)
