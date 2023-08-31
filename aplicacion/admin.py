from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import users
from .models import Pais, Fuerza, Division, Unidad

# Personaliza la visualización de los modelos en el panel de administración
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviacion')
    search_fields = ('nombre', 'abreviacion')

@admin.register(Fuerza)
class FuerzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_filter = ('pais',)
    search_fields = ('nombre',)

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fuerza')
    list_filter = ('fuerza__pais', 'fuerza')
    search_fields = ('nombre',)

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'latitud', 'longitud', 'fuerza', 'division')
    list_filter = ('fuerza__pais', 'fuerza', 'division')
    search_fields = ('nombre', 'fuerza__nombre', 'division__nombre')

# Personaliza la visualización de los usuarios en el panel de administración
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

# Personaliza el título del panel de administración
admin.site.site_header = "Panel de Actividades Presentes y Significativas de las FF.AA. de Países Vecinos"
admin.site.site_title = "Administración de Actividades Presentes y Significativas de las FF.AA. de Países Vecinos"

