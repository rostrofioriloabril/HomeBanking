(function(){
    let lista = document.getElementById('lista'),
        nombreInput = document.getElementById('nombreInput'),
        dineroInput = document.getElementById('dineroInput'),
        btnNuevaPersona = document.getElementById('btn-agregar'),
        resultado = document.getElementById('resultado'),
        total= document.getElementById('total'),
        totalDividido= document.getElementById('totalDividido')
        gastoTotal=0,
        contadorPersonas = 0;
    
    let agregarPersona = function(){
        let nombre = nombreInput.value,
            dinero = dineroInput.value;
        if(dinero<0){
            dinero=''
            dineroInput.style.border=('1px solid red');
        }

        let nuevaPersona = document.createElement('li'),
            contenido = document.createTextNode(nombre+': $'+dinero),
            icono = document.createElement('i');

        icono.className+="fa-solid fa-xmark";

        if(dinero===''  && nombre!=''){
            nuevaPersona='';
            dineroInput.style.border=('1px solid red');
        }
        else if(dinero!=''  && nombre===''){
            nuevaPersona='';
            nombreInput.style.border=('1px solid red');
        }
        else if(dinero===''  && nombre===''){
            nuevaPersona='';
            nombreInput.style.border=('1px solid red');
            dineroInput.style.border=('1px solid red');
        }
        else{
            nombreInput.style.border=('1px solid black');
            dineroInput.style.border=('1px solid black');
        };

        if (nuevaPersona !=''){
            contadorPersonas++;
            gastoTotal += parseFloat(dinero)
            actualizarGastoTotal()
        };

        if(contadorPersonas!=0 && dinero!=0){
            resultado.style.display=('flex')
        };

        lista.appendChild(nuevaPersona);
        nuevaPersona.appendChild(contenido);
        nuevaPersona.appendChild(icono);


        nombreInput.value = '';
        dineroInput.value = '';

        icono.addEventListener('click', function(){
            nuevaPersona.remove();
            contadorPersonas--;
            gastoTotal-=parseFloat(dinero);
            actualizarGastoTotal (gastoTotal);
            if(contadorPersonas==0){
                resultado.style.display=('none')
            }
        });
        
        function actualizarGastoTotal(){
            total.textContent= ('Total: $' + gastoTotal.toFixed(2));
            totalDividido.textContent= ('Cada uno debe poner: $'+ (gastoTotal/contadorPersonas).toFixed(2));
        }
    }
    btnNuevaPersona.addEventListener('click', agregarPersona);
}())





