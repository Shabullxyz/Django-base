# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    codigo_interno = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    unidades_x_paquete = models.IntegerField(default=0)
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=10)

    def __str__(self):
        return self.nombre

