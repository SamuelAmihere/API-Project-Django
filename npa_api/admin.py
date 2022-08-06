from django.contrib import admin
from .models import MarketCategory,Player,Product


# Register your models here.
myModels = [
    MarketCategory,
    Player,
    Product
    ]

admin.site.register(myModels)