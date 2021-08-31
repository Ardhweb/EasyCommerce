from django.contrib import admin
from django.urls import path

from myapp1 import views
from django.conf.urls import url
app_name = 'myapp1'
urlpatterns = [
    path("home", views.index, name='index'),

    path("about", views.about, name='about'),

    path("contact", views.contact, name='contact'),
    
    path('<int:id>/', views.product_detail,
 name='product_detail'),
    
    
    #For Customer Past orders history or Your Orders page
#step02
    path('order-history/',views.order_history,name='your_past_orders'),
    
    path('previous-orders',views.your_orders,name='your_previous_orders'),
   
    
    

    

   


   
    
]