from django.contrib import admin
from .models import Categoria, Etiqueta, Producto, DetalleProducto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "categoria")
    list_filter = ("categoria", "etiquetas")
    search_fields = ("nombre", "descripcion")

@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "producto", "dimensiones", "peso_mb")
    search_fields = ("producto__nombre",)