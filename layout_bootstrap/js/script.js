
const hamburger= document.querySelector('.hamburger');
const introd= document.querySelector('.introduzione');

const menuTendina= document.querySelector('.menu-tendina');
const margineSuperiore= document.querySelector('.marginTop');

const palme2= document.querySelector('.palme2');




/*Si attiva quando la largezza della pagina supera i 1200px*/
/*si attiva all'apertura della pagina web*/
if(window.innerWidth >= 1200){
    //console.log(window);
    //inserisco un'altra immagine
    palme2.childNodes[1].setAttribute('src', './img2.jpg');
    console.log("Larghezza pagina superiore a 1024px");
}




/*click sull'icona hamburger*/
hamburger.addEventListener('click', () => {

    //console.log("premuto");
    /* 
    Recupero l'altezza del menu a tendina per poi assegnarla ad una classe
    appartenetne al div Introduzione per farlo scendere in basso di una dim
    uguale all'altezza del menu a tendina
    const altezzaMenuTendina= menuTendina.style.height;
    const altN= altezzaNav.style.height;
    console.log(altezzaMenuTendina, altN);
    const altezzaTotale= altezzaMenuTendina;

    margineSuperiore.style.marginTop= altezzaTotale;
    console.log(margineSuperiore.style.marginTop);*/

    introd.classList.toggle('marginTop');    
});




//evento sull'oggetto window per rilevare la modifica della dimensione della pagina web (ridimensionamento)
//cioè quando la ridemnsiono
window.addEventListener('resize', () => {
    //larghezza attuale della finestra
    const width = window.innerWidth;
    //console.log(width);

    if(width >= 1200){
        //inserisco un'altra immagine
        palme2.childNodes[1].setAttribute('src', './img2.jpg');
    }
    else if(width < 1200){
        //rimetto l'imagine precedente
        palme2.childNodes[1].setAttribute('src', './img1.jpg');
    }    
});






