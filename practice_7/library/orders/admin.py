from django.contrib import admin
from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display=['itemId', 'created']
    list_display_links=['itemId']
    ordering=['itemId']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'address', 'is_approved', 'email']


admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
