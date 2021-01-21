# Algunas urls de ejemplo. Note las dos ultimas q reciben uno y dos parámetros por la misma url.

from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, despedida, fecha, calculaEdad, curso_django, curso_js

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('chao/', despedida),
    path('fecha/', fecha),
    #path('edadfutura/<int:anio>', calculaEdad),   <---con un parámetro
    path('edadfutura/<int:edad>/<int:anio>', calculaEdad),
    path('plantilla_hija/', curso_django),
    path('plantilla_hija2/', curso_js)
]
