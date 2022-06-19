///--------------------CONTAINER 1-------------------------//
let containerPrincipal = document.getElementById('container_1'),
    meOlvide = document.getElementById('olvidar'),
    nuevoCliente = document.getElementById('nuevo1');


//--------------------CONTAINER 2-------------------------//
let containerAsociate = document.getElementById('container_2'),
    registro = document.getElementById('registro'),
    iniciarSesion = document.getElementById('inicia');


//--------------------CONTAINER 3-------------------------//
let containerRecupera = document.getElementById('container_3'),
    btnIngresar = document.getElementById('ingresar'),
    nuevoCliente2 = document.getElementById('nuevo2');



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



function iniciarSesionFunction (event){
    event.preventDefault();
    containerPrincipal.style.display='block';
    containerAsociate.style.display='none';
    containerRecupera.style.display='none';
}

nuevoCliente2.addEventListener('click',  nuevoRegistro);

 //ESCONDER Y MOSTRAR BALANCE 
//let hideInfoButton: document.getElementById("hideInfo");
//let balanceInfo: document.getElementsByClassName("balance_item");
//
//function hideBalance (){
//    balanceInfo.innerHTML= "XX.XXX;XX"
//}

//hideInfoButton.addEventListener("click", hideBalance);





