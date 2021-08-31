from django.shortcuts import render



# Create your views here.

# Manually Create by Developer
from django.shortcuts import HttpResponse, get_object_or_404
from myapp1.models import Product
from django.template import context
from _ast import Name
from django.http import request
from django.template import Context, loader
from cart.forms import CartAddProductForm
from orders.models import Order, OrderItem
from django.template.defaultfilters import length




# Create your views here.
def index(request ):
    products = Product.objects.all()
   
    return render(request, 'index.html',{'productss':products} )

                                                                                                                                                                                                                                    
# return HttpResponse("This is Home Page for index my Website.")
#about us page
def about(request):
    return HttpResponse("This is Easy Commerce About US Page")

#contact us page

def contact(request):
    return HttpResponse("This is Contact us Page")






#Cart Product Detail Step 6 Cart
def product_detail(request, id, ):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request,'product/detail.html',{'product': product,'cart_product_form': cart_product_form})





#For Customer Past orders history or Your Orders page
#step01


def order_history(request):
    orders = Order.objects.filter(username = request.user.id)
    length = len(orders)
    if length == 0:
        context = {'orders': orders}
    else:
        items = OrderItem.objects.all()
        context = {
        'orders': orders,
        'items': items}
   # orders = Order.objects.filter(username = request.user.id).order_by()

    

    #items = OrderItem.objects.all()


    ##t = loader.get_template('order history.html')
    #c = dict({
      #  'zipped': zip(orders, list(items))
    #})

    #return HttpResponse(t.render(c))
    #context={
        
      # "data": [orders,items]}
    return render(request,'order history.html',context)



def your_orders(request):
    yourorders=Order.objects.filter(username=request.user.id)
    length = len(yourorders)
    if length == 0:
        context={'yourorders':your_orders}
    else:
        yourorderItems=OrderItem.objects.all()
        context={'yourorders':yourorders,' yourorderItems': yourorderItems}
    return  render(request,'previous_orders.html', context)



