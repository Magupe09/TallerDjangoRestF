from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Producto, Ingrediente


class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "inventario/producto_detail.html"


class IngredienteListView(ListView):
    model = Ingrediente
    template_name = "inventario/ingrediente_list.html"


class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = "inventario/ingrediente_detail.html"


class IngredienteCreateView(CreateView):
    model = Ingrediente
    fields = "__all__"
    template_name = "inventario/ingrediente_form.html"
    success_url = reverse_lazy("ingrediente_list")


class IngredienteUpdateView(UpdateView):
    model = Ingrediente
    fields = "__all__"
    template_name = "inventario/ingrediente_form.html"
    success_url = reverse_lazy("ingrediente_list")


class IngredienteDeleteView(DeleteView):
    model = Ingrediente
    template_name = "inventario/ingrediente_confirm_delete.html"
    success_url = reverse_lazy("ingrediente_list")

    ###Product views


class ProductoCreateView(CreateView):
    model = Producto
    fields = ["nombre", "precio_publico", "tipo", "vaso", "volumen_onzas"]
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy("producto_list")


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombre", "precio_publico", "tipo", "vaso", "volumen_onzas"]
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy("producto_list")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "inventario/producto_confirm_delete.html"
    success_url = reverse_lazy("producto_list")
