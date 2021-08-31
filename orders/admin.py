from django.contrib import admin

# Register your models here.

#ORDERS
from .models import Order, OrderItem
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models.aggregates import Count
from django.shortcuts import render



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id__fields = ['product']

    
    
    
    
    

def order_detail(obj):
        url = reverse('orders:admin_order_detail', args=[obj.id])
        return mark_safe(f'<a href="{url}">View</a>')
    
    
    
    
@admin.register(Order)
class OrderAdmin (admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','address','postal_code','city','state','paid','created','updated','username','order_ref',order_detail]
    list_filter = ['paid','created','updated' ,'username']
    
    raw_id__fields = ['username']
    inlines = [OrderItemInline]
    
    
    
    
    
    
    
    #def save_model(self, request, obj, form, change):
        #if getattr(obj, 'customer', None) is None:
        #   obj.customer = request.user
        #obj.save()

    
    