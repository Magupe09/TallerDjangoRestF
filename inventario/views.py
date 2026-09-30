from django.views.generic import ListView, DetailView
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "inventario/producto_detail.html"
