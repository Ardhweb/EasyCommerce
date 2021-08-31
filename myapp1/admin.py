from django.contrib import admin






#Deleting Recent actions on Admin Panel
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


#-----------#
# Register your models here.

from myapp1.models import Product
admin.site.register(Product)
#deleting
admin.site.disable_action('delete_selected')
#class ProductAdmin(admin.ModelAdmin):
   # pass
#admin.site.register(Product, ProductAdmin ),



#Cart


# Define the admin classss