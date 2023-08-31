from rest_framework import serializers
from .models import Pais, Fuerza, Division, Unidad


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class FuerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuerza
        fields = ['id','nombre']

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['id','nombre']
class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['id','nombre','latitud','longitud']






