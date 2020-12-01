from django.urls import path 

#urls that is attached to the method in the view.py  file
from . import views

#defining the url patterns and set that to list
urlpatterns = [
    
    path('contact', views.contact, name = 'contact'),
    
    
]