from django.db import models

# Create your models here.


class Ingrediente(models.Model):
    class Tipo(models.TextChoices):
        BASE = "base", "Base"
        COMPLEMENTO = "complemento", "Complemento"

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    calorias = models.IntegerField()
    inventario = models.IntegerField()
    es_vegetariano = models.BooleanField(default=False)
    es_sano = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    sabor = models.CharField(max_length=100, blank=True)
