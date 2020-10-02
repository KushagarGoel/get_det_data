from django.contrib import admin
from .models import  EmailConfirmed,UserDetails
# Register your models here.

admin.site.register(EmailConfirmed)
admin.site.register(UserDetails)
