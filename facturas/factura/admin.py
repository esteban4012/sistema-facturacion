from django.contrib import admin
from .models import Factura, Articulo

class ArticuloInline(admin.TabularInline):
    model = Articulo
    extra = 1
    fields = ['descripcion', 'valor_unitario', 'cantidad', 'subtotal']
    readonly_fields = ['subtotal']
    show_change_link = True

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'numero_id', 'fecha_creacion', 'total_factura')
    search_fields = ['cliente', 'numero_id']
    list_filter = ['fecha_creacion']
    inlines = [ArticuloInline]
    ordering = ['-fecha_creacion']  # Orden descendente por fecha de creación

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'factura', 'valor_unitario', 'cantidad', 'subtotal')
    list_filter = ['factura']
    search_fields = ['descripcion', 'factura__cliente']
    ordering = ['factura', 'descripcion']  # Ordenar por factura y descripción

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
