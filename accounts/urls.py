from django.urls import path 

#urls that is attached to the method in the view.py  file
from . import views

#defining the url patterns and set that to list
urlpatterns = [
    
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout',views.logout,name = 'logout'),
    path('dashboard',views.dashboard,name = 'dashboard')
    
]