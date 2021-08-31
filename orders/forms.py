from django import forms
from orders.models import Order
from .models import Order



class OrderCreateForm(forms.ModelForm):
    """"""
    
    
    class Meta:
        db_table = 'order'
    
        model = Order
        fields = ['first_name','last_name','email','address',
                    'postal_code','city','state','mobile']
        widgets ={
                
                'first_name':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'last_name':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'email':forms.TextInput(attrs={'class':'form-control w-75 '}),
                'address':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'postal_code':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'city':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'state':forms.TextInput(attrs={'class':'form-control text-center w-75 '}),
                'mobile':forms.TextInput(attrs={'class':'form-control w-75'}),
                
                
                
                }
        #step 01 get username with order in admin
        exclude = ['username', ]
        
    
    
    