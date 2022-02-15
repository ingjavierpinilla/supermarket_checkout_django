from django.contrib import admin
from .models import Product, ShopingBasket, Discount

# Register your models here.
admin.site.register(Product)
admin.site.register(ShopingBasket)
admin.site.register(Discount)
