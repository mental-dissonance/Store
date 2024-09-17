from django.contrib import admin
from .models import Products
from .models import Categories

admin.site.register(Products)
admin.site.register(Categories)