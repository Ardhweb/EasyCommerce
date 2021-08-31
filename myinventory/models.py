from django.db import models

# Create your models here.
from account.models import Profile

from myapp1.models import Product

from django.conf import settings



class Employer(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    fullname=models.CharField(max_length=120,default="")
    phone=models.CharField(max_length=12,default="")
    email=models.EmailField((""), max_length=254,default="")
    address=models.CharField(max_length=300,default="")
    
    
    PRODUCTMANAGER = 'PRODUCT MANAGER'
    GENERALMANAGER = 'GENERAL MANAGER'
    DELIVERY = 'DELIVERY'
    EMPLOYERJOB =     [
        (PRODUCTMANAGER, 'PRODUCTMANAGER'),
        (GENERALMANAGER, 'GENERALMANAGER'),
        (DELIVERY, 'DELIVERY'),
    
    ]
    Employer_job=models.CharField(max_length=200,default="",choices=EMPLOYERJOB)
    
    
    
    
    
    def __str__(self):
        return f'Employer for user {self.user.username}'






