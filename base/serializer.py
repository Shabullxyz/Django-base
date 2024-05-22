from rest_framework import serializers
from .models import Categoria, Proveedor, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields='__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields='__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()
    class Meta:
        model = Producto
        fields=['id', 'nombre','categoria','proveedor','codigo_interno']