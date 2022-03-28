from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

class Company(models.Model):
    companyname = models.CharField(max_length=100)
    regid = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    companyowner = models.CharField(max_length=100)
    websiteid = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    email =models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Candidate(models.Model):
    candidatename = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dob = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
