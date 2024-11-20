from decimal import Decimal
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Factura(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100)
    numero_id = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=100)
    total_factura = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))  

    def actualizar_total(self):
        # Calcular el total sumando los subtotales de todos los artículos relacionados
        total = sum(articulo.subtotal for articulo in self.articulos.all())
        self.total_factura = total
        self.save()

    def __str__(self):
        return f'Factura a nombre de {self.cliente} con C.C. {self.numero_id} con un valor total de {self.total_factura}'


class Articulo(models.Model):
    factura = models.ForeignKey(Factura, related_name='articulos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=3)

    def save(self, *args, **kwargs):
        # Calcular el subtotal antes de guardar el artículo
        self.subtotal = self.valor_unitario * Decimal(self.cantidad)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.descripcion} - {self.cantidad} x {self.valor_unitario}'


# Señales para actualizar el total de la factura al crear o eliminar un artículo
@receiver(post_save, sender=Articulo)
def actualizar_total_factura_al_guardar(sender, instance, **kwargs):
    instance.factura.actualizar_total()


@receiver(post_delete, sender=Articulo)
def actualizar_total_factura_al_eliminar(sender, instance, **kwargs):
    instance.factura.actualizar_total()
