from django.urls import path
from .views import *

urlpatterns = [
    path('Candidatehome/',Candidatehome,name='Candidatehome'),
    path('vacancies/',vacancies,name='vacancies'),
    path('searchvacancy', searchvacancy,name="searchvacancy"),
    path('applyvacancy/<int:id>',apply,name="applyvacancy"),
    path('applyvacancyprocess', applyvacancyprocess,name="applyvacancyprocess"),
    path('calogout/',calogout,name='calogout')
]
