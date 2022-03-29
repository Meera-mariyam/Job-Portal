from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('allcompany/',Allcompany.as_view(),name='allcompany'),
    path('allcandidate',Allcandidate.as_view(),name='allcandidate'),
    path('newcompany/',Newcompany.as_view(),name='newcompany'),
    path('newcandidate/',Newcandidate.as_view(),name='newcandidate'),
    path('Adminhomee/',Adminhomee.as_view(),name='Adminhomee'),
    path('acceptcompany/<int:id>',Acceptcompany.as_view(), name="acceptcompany"),
    path('rejectcompany/<int:id>',Rejectcompany.as_view(), name="rejectcompany"),
    path('acceptcandidate/<int:id>', Acceptcandidate.as_view(), name="acceptcandidate"),
    path('rejectcandidate/<int:id>', Rejectcandidate.as_view(), name="rejectcandidate"),

    path('alogout/',Logout.as_view(),name='alogout')
]