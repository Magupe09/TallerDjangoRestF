from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db import transaction
from .models import Venta


class VentaListView(ListView):
    model = Venta
    template_name = "ventas/venta_list.html"


class VentaCreateView(CreateView):
    model = Venta
    fields = ["producto", "cantidad"]
    template_name = "ventas/venta_form.html"
    success_url = reverse_lazy("venta_list")

    def form_valid(self, form):
        producto = form.cleaned_data["producto"]
        cantidad = form.cleaned_data["cantidad"]

        with transaction.atomic():
            # 1) Revisar inventario
            for ingrediente in producto.ingredientes.all():
                if ingrediente.inventario < cantidad:
                    form.add_error(
                        None, f"Inventario insuficiente de {ingrediente.nombre}"
                    )
                    return self.form_invalid(form)

            # 2) Descontar inventario
            for ingrediente in producto.ingredientes.all():
                ingrediente.inventario -= cantidad
                ingrediente.save()

            # 3) Guardar la venta (seteo usuario y total antes)
            venta = form.save(commit=False)
            venta.usuario = self.request.user
            venta.total = producto.precio_publico * cantidad
            venta.save()

        return redirect(self.success_url)
