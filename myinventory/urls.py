
from django.contrib import admin
from django.urls import path
from myinventory import views
from django.contrib.auth.decorators import login_required
from myinventory.views import order_home


app_name='myinventory'
urlpatterns = [
    
    path('seller',views.seller_home,name="seller_home"),
    
    
    path('seller/orders',views.order_home,name="order_home"),

    

    
    path('seller/invoice/<int:order_id>/', views.orderview,name='orderview'),
    
    path('seller/info/<int:order_id>/', views.order_info, name='orderinfo'),
    
    path('seller/update/<int:order_id>/', views.order_update, name='order_update'),
    
    #login
    path('seller/login/', views.user_login, name='login'),
    


    
]
