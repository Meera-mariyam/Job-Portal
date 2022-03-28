from django.urls import path
from .views import *

urlpatterns = [
    path('Candidatehome/',Candidatehome.as_view(),name='Candidatehome'),
    path('vacancies/',Vacancy.as_view(),name='vacancies'),
    path('searchvacancy', Searchvacancy.as_view(),name="searchvacancy"),
    path('applyvacancy/<int:id>',Apply.as_view(),name="apply"),
    path('applyvacancy/',Applyvacancy.as_view(),name='Applyvacancy'),
    path('calogout/',calogout,name='calogout')
]
