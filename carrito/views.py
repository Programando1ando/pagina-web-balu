from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Carrito
from tienda.models import Producto

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = Carrito.objects.get_or_create(
        usuario=request.user,
        producto=producto,
        defaults={'cantidad': 1}
    )
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('carrito:ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    return render(request, 'carrito/carrito.html', {'carrito_items': carrito_items})  # ✅ Corrección de ruta<<<