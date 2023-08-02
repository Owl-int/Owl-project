const monthYearElement = document.getElementById('monthYear');
const daysElement = document.getElementById('days');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentDate = new Date();

// Función para obtener el nombre del mes con la primera letra en mayúscula
function getCapitalizedMonthName(date) {
  const monthNames = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];
  return monthNames[date.getMonth()];
}

function updateCalendar() {
  const firstDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
  const lastDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);

  monthYearElement.textContent = `${getCapitalizedMonthName(currentDate)} ${currentDate.getFullYear()}`;

  daysElement.innerHTML = '';

  for (let i = 0; i < firstDayOfMonth.getDay(); i++) {
    const emptyDay = document.createElement('div');
    daysElement.appendChild(emptyDay);
  }

  for (let i = 1; i <= lastDayOfMonth.getDate(); i++) {
    const dayElement = document.createElement('div');
    dayElement.textContent = i;
    daysElement.appendChild(dayElement);

    // Si el día es domingo (valor 0 en JavaScript, donde 0 = Domingo, 1 = Lunes, ..., 6 = Sábado), aplicar clase "sunday"
    if (new Date(currentDate.getFullYear(), currentDate.getMonth(), i).getDay() === 0) {
      dayElement.classList.add('sunday');
    }
  }
}

updateCalendar();

prevBtn.addEventListener('click', () => {
  currentDate.setMonth(currentDate.getMonth() - 1);
  updateCalendar();
});

nextBtn.addEventListener('click', () => {
  currentDate.setMonth(currentDate.getMonth() + 1);
  updateCalendar();
});
