const form = document.querySelector(".input-ricerca");

const regex = /^(?!\s*$).+/;


form.addEventListener('keyup', e => {
    
    e.preventDefault();
    
    /*Aggiungi task*/
    
    if (e.key=='Enter' && regex.test(form.add.value)) {
        
        let toDo = form.add.value;
        let li = document.createElement("li");
        let lista = document.querySelector('.ulista')
        
        console.log(toDo);
        
        
        form.add.value = '';
        
        li.innerHTML = `<div>${toDo}</div><div><img src="./images/bin.png" alt="cestino" class="bin"></div>`;

        li.classList.add('elemento-lista') 
        lista.appendChild(li);
        
    }

    /*Cerca Task*/ 
    let ricerca = form.cerca.value;
    
    console.log(ricerca);

    let arrLista = document.querySelectorAll("li");
   

    

   
    arrLista.forEach(elemento => {
    
        

        if (!elemento.innerText.toLowerCase().includes(ricerca.toLowerCase()) && regex.test(ricerca)) {
            elemento.classList.add('hide');
        }else if(e.key=='Backspace'){
            elemento.classList.remove('hide');
        }
    
    }); 
    
    
});


/*Elimina task*/
const cestino = document.querySelector('.bin');
form.addEventListener('click', e => {
    e.preventDefault();
    
    console.log(e);
    
    if (e.target.className==='bin') {
        e.target.parentElement.parentElement.remove();
    }
    
});





