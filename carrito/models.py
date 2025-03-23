from django.db import models
from django.contrib.auth.models import User
from tienda.models import Producto  # Asegúrate de que la app tienda tiene este modelo

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} - {self.usuario.username}'