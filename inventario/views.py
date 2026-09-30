from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from usuarios.decorators import es_empleado_o_admin
from .models import Producto, Ingrediente


class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "inventario/producto_detail.html"


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class IngredienteListView(ListView):
    model = Ingrediente
    template_name = "inventario/ingrediente_list.html"


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = "inventario/ingrediente_detail.html"


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class IngredienteCreateView(CreateView):
    model = Ingrediente
    fields = "__all__"
    template_name = "inventario/ingrediente_form.html"
    success_url = reverse_lazy("ingrediente_list")


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class IngredienteUpdateView(UpdateView):
    model = Ingrediente
    fields = "__all__"
    template_name = "inventario/ingrediente_form.html"
    success_url = reverse_lazy("ingrediente_list")


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class IngredienteDeleteView(DeleteView):
    model = Ingrediente
    template_name = "inventario/ingrediente_confirm_delete.html"
    success_url = reverse_lazy("ingrediente_list")


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class ProductoCreateView(CreateView):
    model = Producto
    fields = ["nombre", "precio_publico", "tipo", "vaso", "volumen_onzas"]
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy("producto_list")


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombre", "precio_publico", "tipo", "vaso", "volumen_onzas"]
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy("producto_list")


@method_decorator(user_passes_test(es_empleado_o_admin), name="dispatch")
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "inventario/producto_confirm_delete.html"
    success_url = reverse_lazy("producto_list")
