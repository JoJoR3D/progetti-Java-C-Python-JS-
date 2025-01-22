
let film= document.querySelector('.schedeFilm');
let searchFilm= document.querySelector('.filmRicercato');


film.addEventListener('click', e =>{  

    if(e.target.parentElement.className == 'div-img-carosello'){

        console.log(e.target.parentElement);

        let elementiFigli= e.target.parentElement.parentElement.children;

        console.log(elementiFigli);

        //mi prendo il titolo del film per passarlo al file js (script6.js) dell'altra pagina html che mi carica tutte le info del film
        console.log(elementiFigli[0].textContent.trim());
        let nome= elementiFigli[0].textContent.trim();
        localStorage.setItem("nome", nome);

        for(let i=0; i < elementiFigli.length; i++){
            if(elementiFigli[i].tagName == 'DIV'){
                if(elementiFigli[i].className != 'div-img-carosello')
                    elementiFigli[i].classList.toggle('show'); 
            }
            
        }
    }
});



//se clicco sul film uscito in seguito alla ricerca
searchFilm.addEventListener('click', e =>{  

    if(e.target.parentElement.className == 'div-img-carosello'){

        console.log(e.target.parentElement);

        let elementiFigli= e.target.parentElement.parentElement.children;

        console.log(elementiFigli);


        //mi prendo il titolo del film per passarlo al file js (script6.js) dell'altra pagina html che mi carica tutte le info del film
        console.log(elementiFigli[0].textContent.trim());
        let nome= elementiFigli[0].textContent.trim();
        localStorage.setItem("nomeSearch", nome);


        for(let i=0; i < elementiFigli.length; i++){
            if(elementiFigli[i].tagName == 'DIV'){
                if(elementiFigli[i].className != 'div-img-carosello')
                    elementiFigli[i].classList.toggle('show'); 
            }
            
        }
    }
});
