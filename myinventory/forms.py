from django import forms


from orders.models import Order


class OrderUpdateForm(forms.ModelForm):
    """"""

    

    class Meta:
        model= Order
        fields= ['order_status','paid','postal_code','state','address','city']
        
        widgets ={
                
                
                'address':forms.TextInput(attrs={'class':'form-control text-center w-50 fs-6 fw-bold'}),
                'postal_code':forms.TextInput(attrs={'class':'form-control text-center w-50 fs-6 fw-bold '}),
                'city':forms.TextInput(attrs={'class':'form-control text-center  w-50 fs-6 fw-bold'}),
                'state':forms.TextInput(attrs={'class':'form-control text-center w-25 fs-6 fw-bold'}),
                'paid':forms.CheckboxInput(attrs={'class':'form-check form-switch form-check-input   btn-block '}),
                'order_status':forms.Select(attrs={'class':'form-select w-50 fs-6 fw-bold'}),
                
                
                
                
                }
        
        
        
#class EmpolyerRegistrationForm(forms.ModelForm):

from .models import Employer
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EmployerEditForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('date_of_birth', 'photo')
