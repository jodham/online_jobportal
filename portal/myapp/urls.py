from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('jobs/', jobs_page, name='jobs')
]
