from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('Blog',views.showthis,name='Blog'),     #step002
    
    path('create/',views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
    
    #3path('orders/order-history',views.order_history,name='your_past_orders'),
    

    
    
    
    
]
