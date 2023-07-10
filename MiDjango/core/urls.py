from django.urls import path, include
from .views import index, accesorios, anillos, aros, collares, pulseras, tobilleras, nosotros, preguntas, producto_form,producto_dele, producto_listar, producto_modificar, menu, ciudad_form, ciudad_dele, ciudad_listar, ciudad_modificar, comuna_dele, comuna_form, comuna_listar, comuna_modificar, tipo_producto_dele, tipo_producto_form, tipo_producto_listar, tipo_producto_modificar, cliente_dele, cliente_form, cliente_listar, cliente_modificar, detalle_venta_form, detalle_venta_listar, venta_dele, venta_form, venta_listar, venta_modificar

urlpatterns = [
    path('', index, name='index'),
    path('accesorios', accesorios, name='accesorios'),
    path('anillos', anillos, name='anillos'),
    path('aros', aros, name='aros'),
    path('collares', collares, name='collares'),
    path('pulseras', pulseras, name='pulseras'),
    path('tobilleras', tobilleras, name='tobilleras'),
    path('nosotros', nosotros, name='nosotros'),
    path('preguntas', preguntas, name='preguntas'),

    path('producto_form', producto_form, name="producto_form"),
    path('producto_dele/<id>', producto_dele, name="producto_dele"),
    path('producto_listar', producto_listar, name="producto_listar"),
    path('producto_modificar/<id>', producto_modificar, name="producto_modificar"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("menu",menu, name='menu'),
    
    path('ciudad_form', ciudad_form, name="ciudad_form"),
    path('ciudad_dele/<id>', ciudad_dele, name="ciudad_dele"),
    path('ciudad_listar', ciudad_listar, name="ciudad_listar"),
    path('ciudad_modificar/<id>', ciudad_modificar, name="ciudad_modificar"),

    path('comuna_form', comuna_form, name="comuna_form"),
    path('comuna_dele/<id>', comuna_dele, name="comuna_dele"),
    path('comuna_listar', comuna_listar, name="comuna_listar"),
    path('comuna_modificar/<id>', comuna_modificar, name="comuna_modificar"),

    path('tipo_producto_form', tipo_producto_form, name="tipo_producto_form"),
    path('tipo_producto_dele/<id>', tipo_producto_dele, name="tipo_producto_dele"),
    path('tipo_producto_listar', tipo_producto_listar, name="tipo_producto_listar"),
    path('tipo_producto_modificar/<id>', tipo_producto_modificar, name="tipo_producto_modificar"),

    path('cliente_form', cliente_form, name="cliente_form"),
    path('cliente_dele/<id>', cliente_dele, name="cliente_dele"),
    path('cliente_listar', cliente_listar, name="cliente_listar"),
    path('cliente_modificar/<id>', cliente_modificar, name="cliente_modificar"),

    path('venta_form', venta_form, name="venta_form"),
    path('venta_dele/<id>', venta_dele, name="venta_dele"),
    path('venta_listar', venta_listar, name="venta_listar"),
    path('venta_modificar/<id>', venta_modificar, name="venta_modificar"),

    path('detalle_venta_form', detalle_venta_form, name="detalle_venta_form"),
    path('detalle_venta_listar', detalle_venta_listar, name="detalle_venta_listar")



]   