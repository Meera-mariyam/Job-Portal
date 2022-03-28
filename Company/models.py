from django.db import models
from Home.models import Company,Login

class Vacancies(models.Model):
    companyid = models.ForeignKey(Company, on_delete=models.CASCADE)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    keyskill = models.CharField(max_length=800)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    experience = models.CharField(max_length=50)
    no_opening = models.IntegerField()
    publishedon = models.CharField(max_length=50)
    lastdate = models.CharField(max_length=50)
    joblocation = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
