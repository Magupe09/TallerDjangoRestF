from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    IngredienteListView,
    IngredienteDetailView,
    IngredienteCreateView,
    IngredienteUpdateView,
    IngredienteDeleteView,
)


urlpatterns = [
    path("productos/", ProductoListView.as_view(), name="producto_list"),
    path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto_detail"),
    path("ingredientes/", IngredienteListView.as_view(), name="ingrediente_list"),
    path(
        "ingredientes/nuevo/",
        IngredienteCreateView.as_view(),
        name="ingrediente_create",
    ),
    path(
        "ingredientes/<int:pk>/",
        IngredienteDetailView.as_view(),
        name="ingrediente_detail",
    ),
    path(
        "ingredientes/<int:pk>/editar/",
        IngredienteUpdateView.as_view(),
        name="ingrediente_update",
    ),
    path(
        "ingredientes/<int:pk>/eliminar/",
        IngredienteDeleteView.as_view(),
        name="ingrediente_delete",
    ),
    path("productos/nuevo/", ProductoCreateView.as_view(), name="producto_create"),
    path(
        "productos/<int:pk>/editar/",
        ProductoUpdateView.as_view(),
        name="producto_update",
    ),
    path(
        "productos/<int:pk>/eliminar/",
        ProductoDeleteView.as_view(),
        name="producto_delete",
    ),
]
