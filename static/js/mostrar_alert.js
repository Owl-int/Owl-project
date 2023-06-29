function alert(message, type) {
  var wrapper = document.createElement('div');
  wrapper.innerHTML =
    '<div class="alert alert-' +
    type +
    ' alert-dismissible" role="alert">' +
    message +
    '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';

  var alertPlaceholder = document.getElementById('liveAlertPlaceholder');
  alertPlaceholder.innerHTML = ''; // Limpiar el contenido existente
  alertPlaceholder.append(wrapper);
}

// Obtiene el parámetro 'success' de la URL
const urlParams = new URLSearchParams(window.location.search);
const successParam = urlParams.get('success');

// Muestra el mensaje si el parámetro 'success' es 'true'
if (successParam === 'true') {
  alert('Se agregó correctamente.', 'success');
}