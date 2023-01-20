from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path('lookupData/', views.index, name='dashBoard'),
   
    
   
]