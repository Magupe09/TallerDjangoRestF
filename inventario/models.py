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

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    class Tipo(models.TextChoices):
        COPA = "copa", "Copa"
        MALTEADA = "malteada", "Malteada"

    nombre = models.CharField(max_length=100)
    precio_publico = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    vaso = models.CharField(max_length=100, blank=True)
    volumen_onzas = models.IntegerField(null=True, blank=True)
    ingredientes = models.ManyToManyField(Ingrediente, through="ProductoIngrediente")

    @property
    def costo(self):
        return sum(i.precio for i in self.ingredientes.all())

    @property
    def calorias(self):
        return sum(i.calorias for i in self.ingredientes.all())

    @property
    def rentabilidad(self):
        return self.precio_publico - self.costo

    def __str__(self):
        return self.nombre


class ProductoIngrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} → {self.ingrediente.nombre}"
