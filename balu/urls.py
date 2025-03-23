from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('tienda.urls')),  # Asegura que esta línea esté aquí
    path('carrito/', include('carrito.urls')),  # Aquí agregamos la app del carrito
    path('accounts/', include('accounts.urls', namespace='accounts')),

]

# Agregar configuración de archivos estáticos y multimedia solo en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)