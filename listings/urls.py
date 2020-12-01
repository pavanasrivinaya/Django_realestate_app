from django.urls import path 

#urls that is attached to the method in the view.py  file
from . import views

#defining the url patterns and set that to list
urlpatterns = [
    #path for nthng that is root path(the home page) and second parameter is that the url is connected to the view.py file
    # view.index(and that method is called index )
    #third parameter is name which is easily access this path 
    path('', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search',views.search,name = 'search')


]