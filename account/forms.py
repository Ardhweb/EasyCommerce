from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    

#
from django.contrib.auth.models import User
from account.models import Profile

class UserRegistrationForm(forms.ModelForm):
    mobile=forms.CharField( label = "Enter Your Mobile.No Here", help_text='Enter Your Mobile .No Here',max_length=13,widget=forms.TextInput(attrs={'class':'form-control text-center w-50 '}) )
    
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control text-center w-50 '}))
    
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control text-center w-50 '}))
    

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email','mobile')
        widgets ={
                'username':forms.TextInput(attrs={'class':'form-control text-center w-50 '}),
                'first_name':forms.TextInput(attrs={'class':'form-control text-center w-50 '}),
                'email':forms.TextInput(attrs={'class':'form-control w-50 '}),
                'mobile':forms.NumberInput(attrs={'class':'form-control w-50'})
                
            }
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    
    #Profiles


class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('first_name', 'last_name','email')
            widgets ={
                'first_name':forms.TextInput(attrs={'class':'form-control text-center w-50 '}),
                'last_name':forms.TextInput(attrs={'class':'form-control text-center w-50 '}),
                'email':forms.TextInput(attrs={'class':'form-control w-50 '}),
                
            }
            
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model =Profile
            fields = ('date_of_birth','photo','phone','first_name','last_name','email')
            widgets ={
                'date_of_birth':forms.TextInput(attrs={'class':'form-control w-50'})
                
                
            }
           
            
    
    
    
##PASSWORD RRESEET


