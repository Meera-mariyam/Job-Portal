from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home_index'),
    path('about/',about,name='home_about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('loginprocess/',loginprocess,name='loginprocess'),
    path('candreg/',candreg,name='candreg'),
    path('candregprocess/',candregprocess,name='candregprocess'),
    path('companyreg/',companyreg,name='companyreg'),
    path('companyregprocess/',companyregprocess,name='companyregprocess'),
]
