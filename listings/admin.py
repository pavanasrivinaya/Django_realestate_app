from django.contrib import admin

# Register your models here.
# Here we are going to customise the code for the admin stuff for the listings app
# listing is present in the listings -> models.py ->class classname need to be given in the import statement
from .models import Listing, Comment



class LisitngAdmin(admin.ModelAdmin):
    #To show the values in the admin side we need to declare this statement
    list_display = ('id','title','is_published','price','list_date','realtor')
   
    #Adding the link to the titles
    list_display_links = ('id','title')
    
    #Adding filter to the realtors which is given in the realtors db
    list_filter = ('realtor',)

    #We can edit the publish checkbox
    list_editable = ('is_published',)

    #we can search for this fields and it also adds the searchbar
    search_fields = ('title','description','city','state','zipcode','price')

    #we can set the number per page(that means it shows only first 25 liust when we search for the specific item)
    list_per_page = 25
    

admin.site.register(Listing, LisitngAdmin)
admin.site.register(Comment)

    