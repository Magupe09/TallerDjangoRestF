from django.contrib import admin
from .models import Ingrediente, Producto, ProductoIngrediente

admin.site.register(Ingrediente)
admin.site.register(Producto)
admin.site.register(ProductoIngrediente)
