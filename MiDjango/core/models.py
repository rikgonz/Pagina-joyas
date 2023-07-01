from django.db import models

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=25)

    def __str__(self):
        return self.nom_ciudad


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=25)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comuna


class TipoProducto(models.Model):
    id_tipo_pro = models.IntegerField(primary_key=True)
    nomb_producto = models.CharField(max_length=30)

    def __str__(self):
        return self.nomb_producto


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nom_producto = models.CharField(max_length=25)
    precio = models.DecimalField(max_digits=25, decimal_places=2)
    stock = models.IntegerField()
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_producto


class Cliente(models.Model):
    id_cli = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    rut = models.CharField(max_length=25)
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    fono = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha_boleta = models.DateField()
    total_boleta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta #{self.id_venta}"


class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Detalle de venta #{self.venta.id_venta}"

