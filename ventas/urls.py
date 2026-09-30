from django.urls import path
from .views import VentaListView, VentaCreateView

urlpatterns = [
    path("ventas/", VentaListView.as_view(), name="venta_list"),
    path("ventas/nueva/", VentaCreateView.as_view(), name="venta_create"),
]
