// Función para obtener la fecha actual en formato yyyy-MM-dd
function obtenerFechaActual() {
    const fechaActual = new Date();
    const year = fechaActual.getFullYear();
    let month = fechaActual.getMonth() + 1;
    let day = fechaActual.getDate();

    // Asegurar que el mes y el día tengan siempre dos dígitos (por ejemplo, 01, 02, ..., 12)
    month = month.toString().padStart(2, '0');
    day = day.toString().padStart(2, '0');

    return `${year}-${month}-${day}`;
}

// Obtener el campo de fecha y establecer el valor inicial en la fecha actual
const fechaInput = document.getElementById("fecha");
fechaInput.value = obtenerFechaActual();

// Agregar evento input al campo de fecha
fechaInput.addEventListener("input", function(event) {
    const fechaSeleccionada = event.target.value;

    // Si la fecha seleccionada es mayor que la fecha actual, restablecerla a la fecha actual
    if (fechaSeleccionada < obtenerFechaActual()) {
        fechaInput.value = obtenerFechaActual();
    }
});