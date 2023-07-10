from django.shortcuts import render
from .models import Producto, Ciudad, Comuna, TipoProducto, Cliente, Venta, DetalleVenta
from .forms import ProductoForm, CiudadForm, ComunaForm, TipoProductoForm, ClienteForm, DetalleVentaForm,VentaForm
from django.contrib.auth.decorators import login_required


def index(request):
    producto = Producto.objects.all()
    datos = {
        "Producto": producto
    }

    return render(request, 'core/index.html', datos)

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


# CRUD PRODUCTOS #

@login_required
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

@login_required
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

@login_required
def producto_listar(request):
    producto = Producto.objects.all()
    datos = {
        "Producto": producto
    }
    return render(request, 'core/producto_listar.html',datos)

@login_required
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

# CRUD CIUDADES #

@login_required
def ciudad_form(request):
    datos = {
        'form': CiudadForm()
    }

    if request.method == 'POST':
        formulario = CiudadForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/ciudad_form.html', datos)

@login_required
def ciudad_dele(request, id):
    ciudad = Ciudad.objects.get(id_ciudad=id)
    datos = {
        'form': CiudadForm(instance=ciudad)
    }

    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST, instance=ciudad)
        ciudad.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/ciudad_dele.html', datos)

@login_required
def ciudad_listar(request):
    ciudad = Ciudad.objects.all()
    datos = {
        "Ciudad": ciudad
    }
    return render(request, 'core/ciudad_listar.html', datos)

@login_required
def ciudad_modificar(request, id):
    ciudad = Ciudad.objects.get(id_ciudad=id)
    datos = {
        'form': CiudadForm(instance=ciudad)
    }

    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST, instance=ciudad)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/ciudad_modificar.html', datos)

# CRUD COMUNAS #
@login_required
def comuna_form(request):
    datos = {
        'form': ComunaForm()
    }

    if request.method == 'POST':
        formulario = ComunaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/comuna_form.html', datos)

@login_required
def comuna_dele(request, id):
    comuna = Comuna.objects.get(id_comuna=id)
    datos = {
        'form': ComunaForm(instance=comuna)
    }

    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST, instance=comuna)
        comuna.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/comuna_dele.html', datos)

@login_required
def comuna_listar(request):
    comuna = Comuna.objects.all()
    datos = {
        "Comuna": comuna
    }
    return render(request, 'core/comuna_listar.html', datos)

@login_required
def comuna_modificar(request, id):
    comuna = Comuna.objects.get(id_comuna=id)
    datos = {
        'form': ComunaForm(instance=comuna)
    }

    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST, instance=comuna)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/comuna_modificar.html', datos)

#CRUD TIPO PRODUCTOS #
@login_required
def tipo_producto_form(request):
    datos = {
        'form': TipoProductoForm()
    }

    if request.method == 'POST':
        formulario = TipoProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/tipo_producto_form.html', datos)

@login_required
def tipo_producto_dele(request, id):
    tipo_producto = TipoProducto.objects.get(id_tipo_pro=id)
    datos = {
        'form': TipoProductoForm(instance=tipo_producto)
    }

    if request.method == 'POST':
        formulario = TipoProductoForm(data=request.POST, instance=tipo_producto)
        tipo_producto.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/tipo_producto_dele.html', datos)

@login_required
def tipo_producto_listar(request):
    tipoproducto = TipoProducto.objects.all()
    datos = {
        "TipoProducto": tipoproducto
    }
    return render(request, 'core/tipo_producto_listar.html', datos)

@login_required
def tipo_producto_modificar(request, id):
    tipo_producto = TipoProducto.objects.get(id_tipo_pro=id)
    datos = {
        'form': TipoProductoForm(instance=tipo_producto)
    }

    if request.method == 'POST':
        formulario = TipoProductoForm(data=request.POST, instance=tipo_producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/tipo_producto_modificar.html', datos)


#CRUD CLIENTE 

@login_required
def cliente_form(request):
    datos = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/cliente_form.html', datos)

@login_required
def cliente_dele(request, id):
    cliente = Cliente.objects.get(id_cli=id)
    datos = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        cliente.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/cliente_dele.html', datos)

@login_required
def cliente_listar(request):
    cliente = Cliente.objects.all()
    datos = {
        "Cliente": cliente
    }
    return render(request, 'core/cliente_listar.html', datos)

@login_required
def cliente_modificar(request, id):
    cliente = Cliente.objects.get(id_cli=id)
    datos = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/cliente_modificar.html', datos)

# CRUD VENTA

@login_required
def venta_form(request):
    datos = {
        'form': VentaForm()
    }

    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/venta_form.html', datos)


def venta_dele(request, id):
    venta = Venta.objects.get(id_venta=id)
    datos = {
        'form': VentaForm(instance=venta)
    }

    if request.method == 'POST':
        formulario = VentaForm(data=request.POST, instance=venta)
        venta.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/venta_dele.html', datos)


def venta_listar(request):
    venta = Venta.objects.all()
    datos = {
        "Venta": venta
    }
    return render(request, 'core/venta_listar.html', datos)


def venta_modificar(request, id):
    venta = Venta.objects.get(id_venta=id)
    datos = {
        'form': VentaForm(instance=venta)
    }

    if request.method == 'POST':
        formulario = VentaForm(data=request.POST, instance=venta)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/venta_modificar.html', datos)

# CRUD DETALLE VENTA
@login_required
def detalle_venta_form(request):
    datos = {
        'form': DetalleVentaForm()
    }

    if request.method == 'POST':
        formulario = DetalleVentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/detalle_venta_form.html', datos)

@login_required
def detalle_venta_dele(request, id):
    detalle_venta = DetalleVenta.objects.get(id=id)
    datos = {
        'form': DetalleVentaForm(instance=detalle_venta)
    }

    if request.method == 'POST':
        formulario = DetalleVentaForm(data=request.POST, instance=detalle_venta)
        detalle_venta.delete()
        datos['mensaje'] = "Eliminado correctamente"

    return render(request, 'core/detalle_venta_dele.html', datos)

@login_required
def detalle_venta_listar(request):
    detallesventa = DetalleVenta.objects.all()
    datos = {
        "DetalleVenta": detallesventa
    }
    return render(request, 'core/detalle_venta_listar.html', datos)

@login_required
def detalle_venta_modificar(request, id):
    detalle_venta = DetalleVenta.objects.get(id=id)
    datos = {
        'form': DetalleVentaForm(instance=detalle_venta)
    }

    if request.method == 'POST':
        formulario = DetalleVentaForm(data=request.POST, instance=detalle_venta)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request, 'core/detalle_venta_modificar.html', datos)

@login_required
def menu(request):

    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context = {"usuario":usuario}
    return render(request, 'registration/menu.html',context)


