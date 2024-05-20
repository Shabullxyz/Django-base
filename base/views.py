from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializer, ProveedorSerializer
from .models import Producto, Proveedor, Categoria

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class ProveedorView(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset= Proveedor.objects.all()

class CategoriaView(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset= Categoria.objects.all()
    