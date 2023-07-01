from django.urls import path, include
from .views import index, accesorios, anillos, aros, collares, pulseras, tobilleras, nosotros, preguntas, producto_form, producto_dele, producto_listar, producto_modificar, menu
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
    path("menu",menu, name='menu')
]   