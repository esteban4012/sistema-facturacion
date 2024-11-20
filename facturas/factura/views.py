from .models import Factura, Articulo
from django.shortcuts import get_object_or_404, render, redirect
from factura.forms import FacturaForm,ArticuloForm,ArticuloFormSet
from decimal import Decimal
from django.contrib import messages


def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        
        if factura_form.is_valid():
            # Guardar la factura primero para obtener su ID
            factura = factura_form.save(commit=False)

            # Inicializar el total de la factura en 0
            total_factura = 0

            # Recibir los datos de los artículos desde el formulario
            descripcion_list = request.POST.getlist('descripcion[]')
            valor_unitario_list = request.POST.getlist('valor_unitario[]')
            cantidad_list = request.POST.getlist('cantidad[]')

            # Guardar la factura para obtener un ID
            factura.save()

            # Crear cada artículo relacionado con la factura
            for i in range(len(descripcion_list)):
                descripcion = descripcion_list[i]
                valor_unitario = Decimal(valor_unitario_list[i])
                cantidad = int(cantidad_list[i])
                subtotal = valor_unitario * cantidad

                # Acumular el subtotal al total de la factura
                total_factura += subtotal

                # Crear y asociar el artículo con la factura guardada
                Articulo.objects.create(
                    factura=factura,
                    descripcion=descripcion,
                    valor_unitario=valor_unitario,
                    cantidad=cantidad,
                    subtotal=subtotal
                )

            # Actualizar el total de la factura y guardar la factura con el total calculado
            factura.total_factura = total_factura
            factura.save()

            # Redirigir a la lista de facturas después de guardar
            return redirect('lista_facturas')

    else:
        factura_form = FacturaForm()
        articulo_form = ArticuloForm()

    return render(request, 'factura/crear_factura.html', {
        'factura_form': factura_form,
        'articulo_form': articulo_form
    })


def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request,'factura/lista_facturas.html', {'facturas':facturas})


def ver_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    articulos = factura.articulos.all()  
    return render(request, 'factura/ver_factura.html', {
        'factura': factura,
        'articulos': articulos
    })



def editar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST, instance=factura)
        articulo_formset = ArticuloFormSet(request.POST, instance=factura)
        
        if factura_form.is_valid() and articulo_formset.is_valid():
            factura_form.save()
            articulo_formset.save()
            return redirect('lista_facturas')
    else:
        factura_form = FacturaForm(instance=factura)
        articulo_formset = ArticuloFormSet(instance=factura)
    
    return render(request, 'factura/editar_factura.html', {
        'factura_form': factura_form,
        'articulo_formset': articulo_formset,
    })



def eliminar_factura(request, factura_id):
    if request.method == 'POST':
        factura = get_object_or_404(Factura, id=factura_id)
        factura.delete()
        messages.success(request, 'La factura ha sido eliminada con éxito.')
    return redirect('lista_facturas')



