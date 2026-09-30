from .models import Usuario


def es_empleado_o_admin(user):
    return user.is_superuser or user.rol in [Usuario.Rol.ADMIN, Usuario.Rol.EMPLEADO]
