const select = document.querySelector('#select');
const opciones = document.querySelector('#opciones');
const salida = document.querySelector('.salida');
const contenidoSelect = document.querySelector('#select .contenido-select');

document.querySelectorAll('#opciones > .opcion').forEach((opcion) => {
	opcion.addEventListener('click', (e) => {
		e.preventDefault();
		contenidoSelect.innerHTML = e.currentTarget.innerHTML;
		select.classList.toggle('active');
		select.style.background="#fff"
		opciones.classList.toggle('active');
	});
});

select.addEventListener('click', () => {
	select.classList.toggle('active');
	opciones.classList.toggle('active');

});
