
const botonRecupera = document.querySelector('.olvidar');
const botonAsociate = document.querySelector('.asociateAqui');
const botonIngresa = document.querySelector('.ingresaAqui');
//          CONTAINERS DE FORMS         ///
const formIngresa = document.querySelector('.ingresa');
const formAsociate = document.querySelector('.asociate');
const formRecupera = document.querySelector('.recupera');

botonRecupera.addEventListener('click',updateFormRecupera);
function updateFormRecupera(){
    formIngresa.style.display = 'none'
    formAsociate.style.display = 'none'
    formRecupera.style.display = 'block'
}

botonAsociate.addEventListener('click',updateFormAsociate);
function updateFormAsociate(){
    formIngresa.style.display = 'none'
    formAsociate.style.display = 'block'
    formRecupera.style.display = 'none'
}

botonIngresa.addEventListener('click',updateFormIngresa);
function updateFormIngresa(){
    formIngresa.style.display = 'block'
    formAsociate.style.display = 'none'
    formRecupera.style.display = 'none'
}