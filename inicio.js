
//------------ formulario | validación ------------//
//Iniciar Sesion//
let dniInput = document.querySelector('.dni');
let userInput = document.querySelector('.user');
let passwordInput = document.querySelector('.password');
let inputsPrimerForm = document.querySelectorAll('.uno')
let nameInput = document.querySelector('.name');
let lastNameInput = document.getElementsByClassName('.lastName');
let ingresar = document.querySelector('.btn-ingresar');
//DATOS GUARDADOS
const dni = ["01234567"];
const user = ["abrilmica"];
const password = ["12345"];
let formulario = document.querySelector('.formulario-ingreso');

ingresar.addEventListener('click', function(event){
    event.preventDefault();

    validarDni();
    validarUser();
    validarPassword();
    if(codigo1,codigo2,codigo3 == true){
        window.location ='index.html';
    }
})
let codigo1 = false;
let codigo2 = false;
let codigo3 = false;
let documento = formulario.dni;
let usuario = formulario.user;
let contrasenhia = formulario.password;



function validarRegistro(){
   // validarName(nombre);
    validarDni();
   validarUser();
   validarPassword();
};
//--------------------------------


function validarDni(){
    for(var i = 0; i < dni.length;i++){
        if((documento.value == dni[i]) || (documento.value.length == 8)){
            console.log("dni correcto")
            documento.style.border='none'
            return codigo1 = true;
        }else{
        documento.value="";
        documento.placeholder= 'dni incorrecto';
        documento.style.border='1px solid rgb(0, 4, 75)'
        documento.style.fontSize='15px';
        return codigo1 = false;
        }
    }
    return codigo1;
}
//     (documento, etc), (dni, etc datos guardados-----------------------------------------------

function validarUser(){
    if(usuario.value.length<8){
       userInput.value="";
       userInput.placeholder='el usuario no es correcto';
       userInput.style.border='1px solid rgb(0, 4, 75)'
       userInput.style.fontSize='15px';
       console.log("usuario incorrecto")
        return codigo2= false;
    }else{ 
        for(var i = 0; i < user.length;i++){
            if((usuario.value == user[i]) || (usuario.value.length > 8 && usuario.value.length<=10)){
                console.log( "correcto")
                usuario.style.border='none'
                return codigo2 = true;
            }
        }
    }
    return codigo2;
};


function validarPassword(){
    for(var i = 0; i < password.length;i++){
    if(contrasenhia.value.length<5){
       contrasenhia.value="";
       contrasenhia.placeholder='contraseña incorrecta';
       contrasenhia.style.border='1px solid rgb(0, 4, 75)'
       contrasenhia.style.fontSize='15px';
       console.log("usuario incorrecto")
       return codigo3 = false;
    }else {
        if((contrasenhia.value.length > 0 && contrasenhia.value.length<=10)||(contrasenhia.value == password[i])){
        contrasenhia.style.border='none'
        return codigo3 = true;
           
        }
    }
    }
return codigo3;
}






//                  Registro               //
let nameUsuario = document.querySelector('.name');
let lastName = document.querySelector('.lastName');
let formRegistro = document.querySelector('.form-registro');
let hijos = document.querySelectorAll('.form-registro input')
let dni2 = document.querySelector('.dni');
let user2 = document.querySelector('.user');
let password2 = document.querySelector('.password');
let passwordRepeatInput = document.querySelector('.passwordRepeat');
let signUp = document.querySelector('.btn-registrarse');
//let nuevoCliente = document.querySelector('')

let nombre = [];
let apellido = [];
let nuevoDni =[];
let nuevoUsuario = [];
let nuevaContasenhia = [];
let valorNombre = formRegistro.name;
let valorApellido = formRegistro.lastName;
let valorDni = formRegistro.dni;
let valorUsuario = formRegistro.user;
let valorConstrasenhia = formRegistro.password;
let valorConstrasenhia2 = formRegistro.passwordRepeat;
let f1 = false;
    f2 = false;    
    f3 = false;
    f4 = false;
    f5 = false;
    f6 = false;

formRegistro.addEventListener("click", (e) => {
    e.preventDefault();
})
const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{5,10}$/, // 6 a 10 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	dni: /^\d{8}$/ // 7 a 14 numeros.
}

function validarNombre(){
        if((expresiones.nombre.test(valorNombre.value) && (valorNombre.value!=nombre[0]))){
            nombre.push(valorNombre.value);
            console.log(nombre);
            nameUsuario.style.border='none'
            return f1=true;
        }else if(valorNombre.value==nombre[0]){
               nombre.pop();
        }else{
            nameUsuario.value="";
            nameUsuario.placeholder='el nombre es incorrecto';
            nameUsuario.style.fontSize='20px';
            nameUsuario.style.border='1px solid rgb(0, 4, 75)';
            return f1=false;
        }
        return f1;
}

function validarApellido(){
    
    if((expresiones.apellido.test(valorApellido.value)) && (valorApellido.value != "")){
        console.log("hecho");
        apellido.push(valorApellido.value);
        console.log(apellido);
        valorApellido.style.border='none'
        return f2=true;
    }else if (valorApellido.value == apellido[0]) {
        apellido.pop();
        return apellido.length-1;
    } else {

       valorApellido.value = "";
       valorApellido.placeholder = 'el apellido es incorrecto';
       valorApellido.style.fontSize = '20px';
       valorApellido.style.border = '1px solid rgb(0, 4, 75)';
       return f2=false;
    }
    return f2;
}/*
hijos.forEach((input) => {
    input.addEventListener('change', validar)
})*/

function validarDni2(){
    if((expresiones.dni.test(valorDni.value))){
        nuevoDni.push(valorDni.value);
        console.log(nuevoDni);
        valorDni.style.border='none'
        return f3=true;
    }else if(valorDni.value==nuevoDni[0]){
           nuevoDni.pop();
    }else{

        valorDni.value="";
        valorDni.placeholder='el dni es incorrecto';
        valorDni.style.fontSize='20px';
        valorDni.style.border='1px solid rgb(0, 4, 75)';
        return f3=false;
    }
    return f3;
}
function validarUsuario1(){
    if((expresiones.usuario.test(valorUsuario.value))){
        nuevoUsuario.push(valorUsuario.value);
        valorUsuario.style.border='none'
        console.log(nuevoUsuario);
        return f4= true;
    }else if(valorUsuario.value==nuevoUsuario[0]){
           nuevoUsuario.pop();
    }else{

        valorUsuario.value="";
        valorUsuario.placeholder='el usuario es incorrecto';
        valorUsuario.style.fontSize='20px';
        valorUsuario.style.border='1px solid rgb(0, 4, 75)';
        return f4=false;
    }
    return f4;
}
function validarPassword1(){
    if((expresiones.password.test(valorConstrasenhia.value))&&(valorConstrasenhia.value != "")){
        nuevaContasenhia.push(valorConstrasenhia.value);
        console.log(nuevaContasenhia);
        valorConstrasenhia.style.border='none'
        return f5=false;

    }else if(valorConstrasenhia.value == nuevaContasenhia[0]){
           nuevaContasenhia.pop();
    }else{
        valorConstrasenhia.value="";
        valorConstrasenhia.placeholder='contraseña incorrecta';
        valorConstrasenhia.style.fontSize='20px';
        valorConstrasenhia.style.border='1px solid rgb(0, 4, 75)';
        return f5=false;
    }
    return f5;
}
function validarPassword2(){
    if((expresiones.password.test(valorConstrasenhia2.value))&& (valorConstrasenhia2.value == valorConstrasenhia.value)&& (valorConstrasenhia2.value != "")){
        valorConstrasenhia2.style.border='none'
        return f6= true;
    }else{
        valorConstrasenhia2.value="";
        valorConstrasenhia2.placeholder='La contraseña no coincide';
        valorConstrasenhia2.style.fontSize='20px';
        valorConstrasenhia2.style.border='1px solid rgb(0, 4, 75)';
        return f6 = false;
        
    }
    return f6;
}



 function validar(){
    validarNombre();
    validarApellido();
    validarDni2();
    validarUsuario1();
    validarPassword1();
    validarPassword2();

 }
signUp.addEventListener("click", (event)=> {
    event.preventDefault();
    validar();
    if (f1,f2,f3,f4,f5,f6 == true){
        containerPrincipal.style.display='block';
        containerAsociate.style.display='none';
        containerRecupera.style.display='none';
    }
});
