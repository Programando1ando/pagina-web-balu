from django.urls import path
from .views import tienda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tienda, name='tienda'),  # Ruta para ver la tienda
]

from django.urls import path
from .views import lista_productos

app_name = 'tienda'


