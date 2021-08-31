from django.db import models
from django.template.defaultfilters import date
from django.db.models import utils
import datetime
from django.utils import timezone
from django.urls import reverse








# Create your models here.

   
#SelfTest

class Product(models.Model):
    
    PRODUCT_TYPE = (
        ('T', 'T-shirt'),
        ('S', 'Shirt'),
        ('W', 'Watch'),
    )
    name = models.CharField( max_length=250)

    
    upload_Image = models.ImageField(upload_to='uploads/',default="True" )
    #upload = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None ,defualt="")
    description = models.TextField(max_length=250)
    product_type = models.CharField(max_length=5, choices=PRODUCT_TYPE,  null=True)
    #meta_keywords = models.CharField(max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufacturer = models.CharField(max_length=300,blank=True)
    #price_in_dollars = models.DecimalField(max_digits=6,decimal_places=2)
    price= models.DecimalField(max_digits=6,decimal_places=2)
    #deleting
    actions = ['delete_selected', 'a_third_action']

# Showing Product Name on listing in Admin Panel---------||||||||>>>>

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return reverse('myapp1:product_detail',args=[self.id, ])


        #for Upload_image models class
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)    


#Cart





        