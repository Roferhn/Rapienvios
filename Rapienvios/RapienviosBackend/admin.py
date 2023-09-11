from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'lastname', 'phone', 'type')

admin.site.register(Shipping_Status)
admin.site.register(Shipping_Type)
admin.site.register(User_Type)
admin.site.register(User, UserAdmin)
admin.site.register(Shipping)
admin.site.register(Pricing)
admin.site.register(Package)
