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

const list = document.getElementById('list-group');
fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then((data) => data.json())
    .then((data) =>
        data.forEach((e) => {
            console.log(e);
            const li = document.createElement('li');
            li.classList.add('list-group-item');
            list.appendChild(li);

			const nombreDolar = document.createElement('h4');
			nombreDolar.innerText = `${e.casa.nombre}`;
			li.appendChild(nombreDolar);
			
			const divCompraVenta = document.createElement('div');
			divCompraVenta.classList.add('div-compra-venta');
			li.appendChild(divCompraVenta);

            const compra = document.createElement('h6');
            compra.innerText = `Compra`;
            divCompraVenta.appendChild(compra);

            const venta = document.createElement('h6');
            venta.innerText = `Venta`;
            divCompraVenta.appendChild(venta);

			const divPreciosDolar = document.createElement('div');
			divPreciosDolar.classList.add('div-precios-dolar');
			li.appendChild(divPreciosDolar);

			const precioCompra = document.createElement('p');
			precioCompra.innerText = `$ ${e.casa.compra}`;
			divPreciosDolar.appendChild(precioCompra);

			const precioVenta = document.createElement('p');
			precioVenta.innerText = `$ ${e.casa.venta}`;
			divPreciosDolar.appendChild(precioVenta);

			
        })
    );