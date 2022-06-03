(function(){
    var lista = document.getElementById('lista'),
        nombreInput = document.getElementById('nombreInput'),
        dineroInput = document.getElementById('dineroInput');
        btnNuevaPersona = document.getElementById('btn-agregar');
        resultado = document.getElementById('resultado');
        dineroTotal=''
    
    var agregarPersona = function(){
        var nombre = nombreInput.value,
            dinero = dineroInput.value;
        if(dineroInput.value==='' && nombreInput.value!=''){
            dinero=0
        };
        if(nombreInput.value==='' && dineroInput.value!=''){
            nombre= 'X'
        };
        var nuevaPersona = document.createElement('li'),
            contenido = document.createTextNode(nombre+': $'+dinero),
            icono = document.createElement('i');
        icono.className+="fa-solid fa-xmark";


        if (nombre==='' && dinero===''){
            nombreInput.setAttribute('placeholder', 'Agregar un nombre valido');
            nombre.className = 'Error';

            dineroInput.setAttribute('placeholder', 'Agregar un valor valido');
            dinero.className = 'Error';
            return false;
        };

        lista.appendChild(nuevaPersona);
        nuevaPersona.appendChild(contenido);
        nuevaPersona.appendChild(icono);


        nombreInput.value = '';
        dineroInput.value = '';

        for(var i=0; i<=lista.children.length -1; i++){
            lista.children[i].addEventListener('click', function(){
                this.parentNode.removeChild(this);
            });
        }
    }

        var comprobarInput = function(){
            nombreInput.className ='';
            nombreInput.setAttribute('placeholder','Agrega un nombre');

            dineroInput.className ='';
            dineroInput.setAttribute('placeholder','Agrega un valor');
        };
    
        btnNuevaPersona.addEventListener('click', agregarPersona);
        nombreInput.addEventListener('click', comprobarInput);
        dineroInput.addEventListener('click', comprobarInput);
}())