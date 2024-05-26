from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Card_number

admin.site.register(Product)
admin.site.register(Card_number)