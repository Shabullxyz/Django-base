from rest_framework import serializers
from .models import TablaScrap

class TablaScrapSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only= True)
    producto_proveedor=serializers.CharField(source='producto.proveedor.nombre', read_only= True)
    producto_codigo_interno=serializers.CharField(source='producto.codigo_interno', read_only= True)

    class Meta:
        model=TablaScrap
        fields='__all__'
