from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UsuarioCreationForm
from .models import Usuario


class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = "usuarios/registro.html"
    success_url = reverse_lazy("login")
