from django.contrib import admin
from .models import Empleado, Cliente, Venta

# Registra tus modelos aquí.
admin.site.register(Empleado)
# admin.site.register(Cliente) # Descomentar cuando se trabaje con clientes
# admin.site.register(Venta)   # Descomentar cuando se trabaje con ventas