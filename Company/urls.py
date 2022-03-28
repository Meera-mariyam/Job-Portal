from django.urls import path
from .views import *

urlpatterns = [
    path('Companyhome/',Companyhome,name='Companyhome'),
    path('addvacancy/',addvacancy,name='addvacancy'),
    path('vacancyprocess/',vacancyprocess,name='vacancyprocess'),
    path('application/',application, name="application"),
    path('idvacancy/<int:id>',idvacancy,name="idvacancy"),
    path('update_comp/<int:id>',update_comp,name='updatecomp'),
    path('updateprocess/<int:id>',updateprocess,name='updateprocess'),
    path('clogout/',clogout,name='clogout')
]