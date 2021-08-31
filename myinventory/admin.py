from django.contrib import admin

# Register your models here.





from django.contrib import admin
from .models import Employer
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo','fullname','email','phone','address','Employer_job']

