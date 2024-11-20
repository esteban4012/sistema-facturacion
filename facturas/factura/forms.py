from django import forms
from django.forms import inlineformset_factory
from .models import Factura, Articulo

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'numero_id', 'direccion', 'email', 'telefono', 'total_factura']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'valor_unitario', 'cantidad', 'subtotal']


# Usamos inlineformset_factory para manejar los artículos asociados a la factura
ArticuloFormSet = inlineformset_factory(
    Factura,  # Modelo principal (Factura)
    Articulo,  # Modelo relacionado (Articulo)
    form=ArticuloForm,  # Formulario de los artículos
    extra=0,  # Número de formularios vacíos que queremos añadir al cargar la página
    can_delete=True  # Permite eliminar artículos si es necesario
)
