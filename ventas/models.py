from django.db import models
from inventario.models import Producto
from django.conf import settings


class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    cantidad = models.IntegerField()

    total = models.DecimalField(max_digits=10, decimal_places=2)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"
