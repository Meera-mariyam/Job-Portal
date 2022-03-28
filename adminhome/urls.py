from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('allcompany/',allcompany,name='allcompany'),
    path('allcandidate',allcandidate,name='allcandidate'),
    path('newcompany/',newcompany,name='newcompany'),
    path('newcandidate/',newcandidate,name='newcandidate'),
    path('Adminhomee/',Adminhomee,name='Adminhomee'),
    path('acceptcompany/<int:id>',acceptcompany, name="acceptcompany"),
    path('rejectcompany/<int:id>',rejectcompany, name="rejectcompany"),
    path('acceptcandidate/<int:id>', acceptcandidate, name="acceptcandidate"),
    path('rejectcandidate/<int:id>', rejectcandidate, name="rejectcandidate"),

    path('alogout/',alogout,name='alogout')
]