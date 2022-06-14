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



//-------------Cambiar Ingresar/registrarse/recuperar ------//

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


//------------ formulario | validación ------------

let dniInput = document.getElementsByClassName('dni'),
    userInput = document.getElementsByClassName('user'),
    passwordInput = document.getElementsByClassName('password'),
    passwordRepeatInput = document.getElementsByClassName('passwordRepeat'),
    nameInput = document.getElementsByClassName('name'),
    lastNameInput = document.getElementsByClassName('lastName'),
    ingresar = document.getElementsByClassName('btn-ingresar'),
    dni = dniInput.value,
    user = userInput.value,
    password = passwordInput.value,
    passwordRepeat = passwordRepeatInput.value,
    name = nameInput.value,
    lastName = lastNameInput.value;
    

function validarIngreso(){
    validarDni(dni);
    validarUser(user);
    validarPassword(password);
}
function validarRegistro(){
    validarName(name);
    validarDni(dni);
    validarUser(user);
    validarPassword(password);
}
function validarDni(dni){
    if(dni.length<8 || dni.length>8){
        dniInput.style.border=('1px solid red !important');
    }
}
function validarUser(user){
    if(user.length<8){
        userInput.style.border=('1px solid red !important');
    }
}
function validarPassword(password){
    if(password.length<8){
        passwordInput.style.border=('1px solid red !important');
    }
    if (passwordRepeat!=''){
        if(password!=passwordRepeat){
            passwordInput.style.border=('1px solid red !important');
            passwordRepeatInput.style.border=('1px solid red !important');
        }
    }
}
function validarName(name){
    const letras = new RegExp("^[a-zA-Z ]+$");
    return letras.test(name);
}

ingresar.addEventListener('click', validarIngreso);







