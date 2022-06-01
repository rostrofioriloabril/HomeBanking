///--------------------CONTAINER 1-------------------------//
var containerPrincipal = document.getElementById('container_1');
var meOlvide = document.getElementById('olvidar');
var nuevoCliente = document.getElementById('nuevo1');


//--------------------CONTAINER 2-------------------------//
var containerAsociate = document.getElementById('container_2');
var registro = document.getElementById('registro')
var iniciarSesion = document.getElementById('inicia');


//--------------------CONTAINER 3-------------------------//
var containerRecupera = document.getElementById('container_3');
var btnIngresar = document.getElementById('ingresar');
var nuevoCliente2 = document.getElementById('nuevo2');









//-------------FUNCIONES Y BOTONES------//

function nuevoRegistro(event){
    event.preventDefault();
    containerAsociate.style.display='block'
    containerPrincipal.style.display='none';
    containerRecupera.style.display='none';
}
nuevoCliente.addEventListener('click', nuevoRegistro);

function datosOlvidados(event){
    event.preventDefault(),
    containerPrincipal.style.display='none';
    containerAsociate.style.display='none';
    containerRecupera.style.display='block';
}
meOlvide.addEventListener('click', datosOlvidados);


iniciarSesion.addEventListener('click', iniciarSesionFunction);
registro.addEventListener('click',nuevoRegistro);


function iniciarSesionFunction (event){
    event.preventDefault();
    containerPrincipal.style.display='block';
    containerAsociate.style.display='none';
    containerRecupera.style.display='none'
}
btnIngresar.addEventListener('click',iniciarSesionFunction);
nuevoCliente2.addEventListener('click',  nuevoRegistro);




