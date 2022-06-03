(function(){
    let lista = document.getElementById('lista'),
        nombreInput = document.getElementById('nombreInput'),
        dineroInput = document.getElementById('dineroInput'),
        btnNuevaPersona = document.getElementById('btn-agregar'),
        resultado = document.getElementById('resultado'),
        total= document.getElementById('total'),
        labelDinero= document.getElementById('labelDinero'),
        labelNombre= document.getElementById('labelNombre'),
        gastoTotal=0,
        contadorPersonas = 0;
    

    let agregarPersona = function(){
        let nombre = nombreInput.value,
            dinero = dineroInput.value;
        if(dinero<0){
            dinero=0
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
            nuevaPersona=''
        }
        else{
            nombreInput.style.border=('1px solid black');
            dineroInput.style.border=('1px solid black');
        };

        if (nuevaPersona !=''){
            contadorPersonas++;
            gastoTotal += parseFloat(dinero)
        };

        if(contadorPersonas!=0 && dinero!=0){
            resultado.style.display=('flex')
        };

        lista.appendChild(nuevaPersona);
        nuevaPersona.appendChild(contenido);
        nuevaPersona.appendChild(icono);


        nombreInput.value = '';
        dineroInput.value = '';

        for(var i=0; i<=lista.children.length -1; i++){
            icono.addEventListener('click', function(){
                nuevaPersona.remove();
                contadorPersonas-=1;
                gastoTotal-=parseFloat(dinero)
                if(contadorPersonas==0){
                    resultado.style.display=('none')
                }
            });
        }
        gastoTotalFormateado=(gastoTotal/contadorPersonas).toFixed(2)
        total.textContent= ('Total: $' +gastoTotal.toFixed(2));
        totalDividido.textContent= ('Cada uno debe poner: $'+ gastoTotalFormateado);
    }
    btnNuevaPersona.addEventListener('click', agregarPersona);
}())






