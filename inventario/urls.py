from django.urls import path
from .views import ProductoListView, ProductoDetailView


urlpatterns = [
    path("productos/", ProductoListView.as_view(), name="producto_list"),
    path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto_detail"),
]
