from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='home_index'),
    path('about/',About.as_view(),name='home_about'),
    path('contact/',Contact.as_view(),name='contact'),
    path('login/',LoginView.as_view(),name='login'),
    path('candreg/',Candreg.as_view(),name='candreg'),
    path('companyreg/',Companyreg.as_view(),name='companyreg'),
]
