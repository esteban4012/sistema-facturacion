document.addEventListener('DOMContentLoaded', () => {
    // Añadir los eventos a los campos originales si existen
    const originalItemRow = document.querySelector('.item-row');
    if (originalItemRow) {
        addEventListenersToNewItem(originalItemRow);
    }

    // Recalcular el subtotal y el total cuando la página se cargue
    updateSubtotalAndTotal();
});

function addItem() {
    // Seleccionar el contenedor de los items
    const itemsContainer = document.querySelector('.items-container');

    // Seleccionar la última fila de items para clonarla
    const lastItemRow = document.querySelector('.item-row');

    // Clonar la fila de items
    const newItemRow = lastItemRow.cloneNode(true);

    // Limpiar los campos del nuevo item
    newItemRow.querySelectorAll('input').forEach(input => {
        input.value = '';
        if (input.name === "subtotal[]") {
            input.readOnly = true;
        }
    });

    // Mostrar el botón de eliminar en la fila clonada
    const deleteButton = newItemRow.querySelector('.delete-item-btn');
    deleteButton.style.display = 'inline-block';  // Mostrar el botón de eliminar

    // Asegurarse de que el botón de eliminar tenga la funcionalidad correcta
    deleteButton.onclick = function() {
        newItemRow.remove();
        updateSubtotalAndTotal();
    };

    // Añadir la nueva fila al contenedor de items
    itemsContainer.appendChild(newItemRow);

    addEventListenersToNewItem(newItemRow);
}

function addEventListenersToNewItem(itemRow) {
    const unitPriceInput = itemRow.querySelector('input[name="valor_unitario[]"]');
    const quantityInput = itemRow.querySelector('input[name="cantidad[]"]');
    const subtotalInput = itemRow.querySelector('input[name="subtotal[]"]');

    // Al cambiar valor unitario o cantidad, recalcular el subtotal
    unitPriceInput.addEventListener('input', () => updateSubtotalAndTotal());
    quantityInput.addEventListener('input', () => updateSubtotalAndTotal());
}

function updateSubtotalAndTotal() {
    const itemRows = document.querySelectorAll('.item-row');
    let total = 0;

    itemRows.forEach(row => {
        const unitPrice = parseFloat(row.querySelector('input[name="valor_unitario[]"]').value) || 0;
        const quantity = parseInt(row.querySelector('input[name="cantidad[]"]').value) || 0;
        const subtotal = unitPrice * quantity;
        row.querySelector('input[name="subtotal[]"]').value = subtotal.toFixed(2);

        total += subtotal;
    });

    // Actualizar el total de la factura
    const totalFacturaInput = document.querySelector('input[name="total_factura"]');
    totalFacturaInput.value = total.toFixed(2);
}

