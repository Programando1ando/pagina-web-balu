from django.urls import path
from .views import agregar_al_carrito, ver_carrito

app_name = 'carrito'  # Asegura que esto está presente

urlpatterns = [
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', ver_carrito, name='ver_carrito'),
]