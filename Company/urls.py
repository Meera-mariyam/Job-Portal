from django.urls import path
from .views import *

urlpatterns = [
    path('Companyhome/',Companyhome.as_view(),name='Companyhome'),
    path('addvacancy/',Addvacancy.as_view(),name='addvacancy'),
    path('application/',Application.as_view(), name="application"),
    path('clogout/',Clogout.as_view(),name='clogout')
]