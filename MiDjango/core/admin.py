from django.contrib import admin
from .models import Ciudad, Comuna, TipoProducto, Producto, Cliente, Venta, DetalleVenta

admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
