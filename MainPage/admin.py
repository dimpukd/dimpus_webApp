from django.contrib import admin

# Register your models here.

from .models import food,wine,other_products

admin.site.register(food)
admin.site.register(wine)
admin.site.register(other_products)


