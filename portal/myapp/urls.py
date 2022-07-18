from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs_page, name='jobs'),
    path('profile/', views.profile, name='profile')
]
