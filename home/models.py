from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Proveedor(models.Model):
    rutProveedor = models.CharField(max_length=10)
    dvProveedor = models.CharField(max_length=1)
    nombreProveedor = models.CharField(max_length=50)
    fonoProveedor = models.CharField(max_length=20)
    correoProveedor = models.EmailField(max_length=50)
    direccionProveedor =  models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nombreProveedor
    
class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,serialize=False,max_length=10)
    nombreProducto = models.CharField(max_length=50)
    descripcionProducto = models.CharField(max_length=50)
    precioProducto = models.IntegerField
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreProducto


# class Usuario(models.Model):
#     nombreUsuario = models.TextField
#     contraseña = models.
#     usuarioRut


# class Administrador(models.Model):
#     rutAdmin = models.CharField(max_length=20)
#     dvAdmin = models.CharField(max_length=1)
#     nombreAdmin = models.CharField(max_length=50)
#     apellidoAdmin = models.CharField(max_length=50)
#     correoAdmin = models.EmailField(max_length=50)
#     fonoAdmin = models.CharField(max_length=20)

# class Cliente(models.Model):
#     rutCliente = models.CharField(max_length=20)
#     dvCliente = models.CharField(max_length=1)
#     nombreCliente = models.CharField(max_length=50)
#     apellidoCliente = models.CharField(max_length=50)
#     fonoCliente = models.CharField(max_length=20)
#     correoCliente = models.EmailField(max_length=50)
#     direccionCliente = models.EmailField(max_length=100)
#     nombreUsuarioCli = models.CharField(max_length=50)
    
# class Empleado(models.Model):
#     rutEmpleado = models.CharField(max_length=20)
#     dvEmpleado = models.CharField(max_length=1)
#     nombreEmpleado = models.CharField(max_length=50)
#     apellidoEmpleado = models.CharField(max_length=50)
#     fonoEmpleado = models.CharField(max_length=20)
#     correoEmpleado = models.EmailField(max_length=50)
#     direccionEmpleado = models.EmailField(max_length=100)
#     nombreUsuarioEmp = models.CharField(max_length=50)

