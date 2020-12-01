from django.db import models
from datetime import datetime, date
from realtors.models import Realtor
from django.core.validators import MinValueValidator, MaxValueValidator 

# Create your models here.
# Here we are going to create a model by using the class
class Listing(models.Model):
    #Properties
    # It is the most difficult  one because it is the most part of another tables and it is a Foreign key for other tables 
    #first parameter is taking the model that is relating to the other model
    realtor = models.ForeignKey(Realtor,on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField('message')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    proid = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name= "id+")
    date_comment = models.DateField(default = date.today)