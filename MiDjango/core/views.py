from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def accesorios(request):
    return render(request, 'core/accesorios.html')

def anillos(request):
    return render(request, 'core/anillos.html')

def aros(request):
    return render(request, 'core/aros.html') 

def collares(request):
    return render(request, 'core/collares.html')
 
def pulseras(request):
    return render(request, 'core/pulseras.html')

def tobilleras(request):
    return render(request, 'core/tobilleras.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def preguntas(request):
    return render(request, 'core/preguntas.html') 



# Create your views here.

def producto_form(request):
    datos = {
        'form': ProductoForm()
    }

    if request.method=='POST':
        formulario= ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"


    return render(request, 'core/producto_form.html', datos)


def producto_dele(request, id):
    aut = Producto.objects.get(id_producto=id)
    datos = {
        'form': ProductoForm(instance=aut)
    }
    if request.method=='POST':
        formulario= ProductoForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado Correctamente"

    return render(request, 'core/producto_dele.html', datos)


def producto_listar(request):
    producto = Producto.objects.all()
    datos = {
        "Producto": producto
    }
    return render(request, 'core/producto_listar.html',datos)

def producto_modificar(request, id):
    arreglo = Producto.objects.get(id_producto=id)
    datos = {
        'form': ProductoForm(instance=arreglo)
    }
    if request.method=='POST':
        formulario= ProductoForm(data=request.POST, instance=arreglo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/producto_modificar.html', datos)

@login_required
def menu(request):

    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context = {"usuario":usuario}
    return render(request, 'registration/menu.html',context)
