# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_people, name='all_people'),
    path('add/', views.add_person, name='add_person'),
]
