from django.db import models

# Create your models here.
# ORDERS
from myapp1.models import Product
from django.contrib.auth.models import User
from account.forms import User
from django.conf import settings
from django.forms import forms
from decimal import Decimal
from django.db import models
import uuid





User = settings.AUTH_USER_MODEL 

class Order(models.Model):
    order_status=(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivery','Out for delivery'),
        ('Dispatch','Dispatch'),('Cancelled','Cancelled')
    )
    first_name = models.CharField(max_length=50,)
    last_name =  models.CharField(max_length=50)
    email =      models.EmailField()
    mobile =    models.CharField(max_length=13,default="")
    address =    models.CharField(max_length=250)
    postal_code =models.CharField(max_length=20)
    city =       models.CharField(max_length=100)
    state =       models.CharField(max_length=100,default='')
    created =    models.DateTimeField(auto_now_add=True)
    updated =    models.DateTimeField(auto_now=True)
    order_status=models.CharField(max_length=100,null=True,choices=order_status)
    paid =       models.BooleanField(default=False)

    

    
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #stepreference number 01 get username with order in admin
    
    
    order_ref = models.CharField( default=uuid.uuid4().hex[:12].upper(), max_length=12, editable=False)
    
    
    def __str__(self):
        return str(self.order_ref)
    
    
    




        
        
        
    class Meta:
        ordering = ('-created',)
        
        
        
        
    def __str__(self):
        return f'order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    
    #def __str__(self):
        #return "{0}-{1}-{2}".format(self.id, self.created, self.username)

    
    


    
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    ref_id=models.ManyToManyField('Order',related_name='ref_id',db_constraint=True,)
    

    
    
    
    
    
    def __str__(self):
        return str(self.id)
    
    
    def get_cost(self):
        return self.price * self.quantity
    
    









    
    
    
    
    


    

    
    


    

        


    
    

    
    
    
    
    
    
