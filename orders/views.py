from django.shortcuts import get_object_or_404, render

# Create your views here.
#ORDERS
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User
from test.dtracedata import instance
from .models import Order
from django.http.response import HttpResponse
from account.models import Profile






def order_create(request):
        
        cart = Cart(request)
        current_user = request.user
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                #clear the cart
                cart.clear()
                #step 01 get username with order in admin
                # get logged username in model field with foreignkey
                form = form.save(commit=False)
                form.username = request.user
                form.save()
                # get logged username in model field with foreignkey
                
                return render(request, 'orders/order/created.html',{'order':order})
                
                # here if user.is_auntehticated
                
                
        else:
            form = OrderCreateForm()
        return render (request,'orders/order/create.html',{'cart':cart,'form':form},)
        
        
        
    
    
    
    
                    

                    
        
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from itertools import count
from myapp1.models import Product



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})
##For Customer username and User Id Step 2 in view.py




#Total
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.models import  Order
import sqlite3 
from sqlite3 import Error 
from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.aggregates import Count








#status

def total(request):
    
    total_oder=Order.objects.all().count()
    
    context={'total_oder':total_oder}
    
    return render(request,'orders/statistics.html',context)    







#ssttep 01
from django.shortcuts import render
from .models import Order,Product

from account.models import Profile


def showthis(request):
    
    count= Order.objects.all().count()
    
    total_pro=Product.objects.all().count()
    
    total_customers=Profile.objects.all().count()
    
    context= {'count': count,'total_pro':total_pro,'total_customers':total_customers}
        
    return render(request, 'Blog/home.html', context)





    
    
'''
def order_history(request):
    orders = Order.objects.filter(username = request.user.id)
    items = OrderItem.objects.all()
    context = {
        'orderss': orders,
        'items': items
    }
    return render(request, "order history.html", context)
'''


