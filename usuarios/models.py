from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMIN = "admin", "Administrador"
        EMPLEADO = "empleado", "Empleado"
        CLIENTE = "cliente", "Cliente"

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.CLIENTE,
    )
