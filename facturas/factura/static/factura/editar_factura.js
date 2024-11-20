// --------------- CONFIGURACIÓN INICIAL ---------------
document.addEventListener('DOMContentLoaded', () => {
    setupDynamicCalculations(); // Configurar cálculos dinámicos
    updateDeleteCheckboxes();   // Configurar eventos para checkboxes de eliminación
});

// --------------- FUNCIONES PRINCIPALES ---------------

// Agregar un nuevo formulario de artículo al formset
function addItem() {
    const formsetContainer = document.querySelector('.items-container'); // Contenedor de los artículos
    const totalForms = document.getElementById('id_articulos-TOTAL_FORMS'); // Management form

    if (!formsetContainer || !totalForms) {
        console.error("No se encontró el contenedor del formset o el management_form.");
        return;
    }

    const formCount = parseInt(totalForms.value);
    const lastForm = formsetContainer.querySelector('.item-row:last-child'); // Última fila

    if (!lastForm) {
        console.error("No se encontró el último formulario. Asegúrate de que hay al menos un formulario inicial.");
        return;
    }

    const newForm = cloneForm(lastForm, formCount);
    formsetContainer.appendChild(newForm); // Agregar nuevo formulario al contenedor
    totalForms.value = formCount + 1; // Incrementar el total de formularios

    updateDeleteCheckboxes(); // Actualizar eventos de los checkboxes de eliminación
    updateTotalFactura();     // Recalcular el total
    console.log(`Formulario agregado. Total forms: ${totalForms.value}`);
}

// Configurar eventos dinámicos para calcular subtotales y total
function setupDynamicCalculations() {
    const container = document.querySelector('.items-container');
    if (!container) return;

    // Detectar cambios en cantidad y valor unitario
    container.addEventListener('input', event => {
        const target = event.target;
        if (target.name.includes('-cantidad') || target.name.includes('-valor_unitario')) {
            updateSubtotal(target); // Actualizar subtotal dinámicamente
        }
    });
}

// Configurar eventos para checkboxes de eliminación
function updateDeleteCheckboxes() {
    const deleteCheckboxes = document.querySelectorAll('input[type="checkbox"][name*="DELETE"]');
    deleteCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const itemRow = this.closest('.item-row'); // Fila asociada
            const subtotalInput = itemRow.querySelector('input[name*="-subtotal"]');
            const subtotal = parseFloat(subtotalInput.value) || 0;

            if (this.checked) {
                itemRow.classList.add('marked-for-deletion'); // Marcar visualmente
                subtractFromTotal(subtotal); // Restar subtotal al total
            } else {
                itemRow.classList.remove('marked-for-deletion'); // Quitar marca
                addToTotal(subtotal); // Sumar subtotal al total
            }
        });
    });
}

// --------------- FUNCIONES DE CÁLCULO ---------------

// Actualizar el subtotal de una fila
function updateSubtotal(input) {
    const row = input.closest('.item-row');
    const cantidadInput = row.querySelector('input[name*="-cantidad"]');
    const valorUnitarioInput = row.querySelector('input[name*="-valor_unitario"]');
    const subtotalInput = row.querySelector('input[name*="-subtotal"]');

    if (cantidadInput && valorUnitarioInput && subtotalInput) {
        const cantidad = parseFloat(cantidadInput.value) || 0;
        const valorUnitario = parseFloat(valorUnitarioInput.value) || 0;
        const subtotal = cantidad * valorUnitario;

        subtotalInput.value = subtotal.toFixed(2); // Actualiza el subtotal con 2 decimales
        updateTotalFactura(); // Recalcula el total general
    }
}

// Recalcular el total de la factura
function updateTotalFactura() {
    const subtotalInputs = document.querySelectorAll('input[name*="-subtotal"]');
    let totalFactura = 0;

    subtotalInputs.forEach(input => {
        const row = input.closest('.item-row');
        const isDeleted = row.querySelector('input[type="checkbox"][name*="DELETE"]').checked;
        if (!isDeleted) {
            totalFactura += parseFloat(input.value) || 0;
        }
    });

    // Actualizar el campo de Total Factura
    const totalFacturaField = document.querySelector('#id_total_factura');
    if (totalFacturaField) {
        totalFacturaField.value = totalFactura.toFixed(2);
    }
}

// Restar un valor del total de la factura
function subtractFromTotal(amount) {
    const totalFacturaField = document.querySelector('#id_total_factura');
    if (totalFacturaField) {
        let currentTotal = parseFloat(totalFacturaField.value) || 0;
        totalFacturaField.value = (currentTotal - amount).toFixed(2);
    }
}

// Sumar un valor al total de la factura
function addToTotal(amount) {
    const totalFacturaField = document.querySelector('#id_total_factura');
    if (totalFacturaField) {
        let currentTotal = parseFloat(totalFacturaField.value) || 0;
        totalFacturaField.value = (currentTotal + amount).toFixed(2);
    }
}

// --------------- FUNCIONES AUXILIARES ---------------

// Clonar un formulario y actualizar sus índices
function cloneForm(form, index) {
    const newForm = form.cloneNode(true);

    // Actualizar los índices de los inputs en el nuevo formulario
    newForm.querySelectorAll('input, select, textarea').forEach(input => {
        const oldName = input.name;
        const oldId = input.id;

        if (oldName && oldId) {
            // Reemplazar índices en name y id
            input.name = oldName.replace(`-${index - 1}-`, `-${index}-`);
            input.id = oldId.replace(`-${index - 1}-`, `-${index}-`);
        }

        if (input.type !== 'hidden') input.value = ''; // Limpiar valores visibles
        if (input.type === 'checkbox') input.checked = false; // Limpiar checkbox
    });

    return newForm;
}
