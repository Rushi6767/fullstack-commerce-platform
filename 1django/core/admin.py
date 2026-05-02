from django.contrib import admin
from .models import DemoModel, Customer, Order, Contact

# Register your models here.

admin.site.register(DemoModel)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contact)