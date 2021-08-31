from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.





from orders.models import Order, OrderItem
from  myapp1.models import Product

from account.models import Profile


def seller_home(request):
        total_order2=Order.objects.all().count()
        total_product2=Product.objects.all().count()
        total_customer2=Profile.objects.all().count() 
        pending_order=Order.objects.all().filter(order_status='Pending').count()
        order_list=Order.objects.all() #FOR ORDER TAABLE USING FORLOOOP
        myorders=OrderItem.objects.all() 
        context={'total_order2':total_order2,'total_product2':total_product2,'total_customer2':total_customer2,'pending_order':pending_order}
        return render(request,'myhome.html',context)


from django.contrib.admin.views.decorators import staff_member_required


##For Customer username and User Id Step 2 in view.py


@staff_member_required
def orderview(request, order_id):
        order_detail =get_object_or_404(Order, id=order_id)
        return render(request,'seller/orders_app/order/Invoice_order.html',{'order_detail':order_detail})


@staff_member_required
def order_info(request, order_id):
        order_info =get_object_or_404(Order, id=order_id)
        return render(request,'seller/orders_app/order/order_info.html',{'order_info':order_info})




from django.shortcuts import render

from .forms import OrderUpdateForm
from django.contrib import messages
from account.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.http import request



@staff_member_required
def order_update(request, order_id):
        order_edit=get_object_or_404(Order,id=order_id)
        if request.method == 'POST':
                update_form =OrderUpdateForm(instance=order_edit,data=request.POST)
                
                if update_form.is_valid():
                        update_form.save()
                        messages.success(request, 'Order is updated '\
                                'successfully')
                else:
                        messages.error(request, 'Error updating your profile') 
        else:
                update_form =OrderUpdateForm(instance=order_edit)
        return render(request,'seller/orders_app/order/updated.html',{'update_form':update_form})
        



# Order

@staff_member_required
def order_home(request):
        order_list=Order.objects.all() #FOR ORDER TAABLE USING FORLOOOP
        myorders=OrderItem.objects.all() 
        
        context={ 'order_list':order_list,'myorderss':myorders}
        return render(request,"seller/orders_app/order/order.html",context)     
        






#AUTH  LOOGIN
from django.contrib.auth import authenticate ,login
from account.forms import LoginForm

def user_login(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        cd = form.cleaned_data
                        user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
                        if user is not None:
                                if user.is_active:
                                        login(request, user)
                                        return redirect('/seller')
                                else:
                                        return HttpResponse('Disabled account')
                        else:
                                return HttpResponse('Invalid login')
        else:
                form = LoginForm()
        return render(request, 'seller/user/login.html', {'form': form})
