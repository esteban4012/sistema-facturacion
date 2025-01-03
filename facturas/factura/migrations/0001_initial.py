# Generated by Django 5.1.3 on 2024-11-20 02:42

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.CharField(max_length=100)),
                ('numero_id', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=100)),
                ('total_factura', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=3, max_digits=12)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='factura.factura')),
            ],
        ),
    ]
