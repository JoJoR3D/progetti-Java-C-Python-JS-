
const navbar= document.querySelector('.navbar');
const imgSwiper= document.querySelector('.imgSwiper');
const pSwiper= document.querySelector('.p-swiper');
const h1Swiper= document.querySelector('.h1-slide'); 
const buttonSwiper= document.querySelector('.bottone-slide');

const hamburger= document.querySelector('.hamburger');
const mioSwiper= document.querySelector('.mioSwiper');
const dropdown= document.querySelector('.dropdown');

const barraNavigazione= document.querySelector('.barra-navigazione');

const frecciaQuadrato= document.querySelector('.freccia-quadrato');




/*attuale altezza della navbar*/
/* viene eseguito solo al primo avvio della pagina web per far si che ci sia
una giusta distanza tra la navbar e lo swiper fin dal primo avvio e non solo con i
successivi resize (codice sottostante) */
let cont= 0;
if(cont == 0){
    let altezza= String(navbar.offsetHeight)
    mioSwiper.style.marginTop= altezza + "px";

    /*rendo la navbar responsive impostando la sua larghezza, alla prima apertura della
    pagina web, uguale alla larghezza dello swiper. Faccio ciò a causa di position:fixed
    che ho applicato alla navbar che gli attribuisce una larghezza maggiore rispetto 
    alla larghezza della pagina web*/
    //console.log(mioSwiper.offsetWidth);
    let l= String(mioSwiper.offsetWidth);
    barraNavigazione.style.width= l + "px";

    cont++;
}



/* Alla prima apertura della pagina web verifica la larghezza della pagina e se è superiore
a 992px inserisce questo testo nel pulsante della navbar. Sotto lo verifica anche nel caso
venga eseguito un resize della pagina. */
let bottoneStarted= document.querySelector('.bottone-started');
if(window.innerWidth >= 992){
    console.log(window.innerWidth);
    bottoneStarted.textContent= "Get Started"
}



/* EVENTO RESIZE */
/* 
ad ogni ridimensionamento della pagina calcolo l'altezza della navbar e 
applico quel valore come valore della proprietà margin-top dello swiper sottostante
per far si che ad ogni ridimensionamento lo swiper si sempre separato correttamente
dalla navbar. 
Per far ciò uso il localStorage per confrontare il precedente size della pagina con quello
attuale. Il codice viene eseguito solo se il precedente size è diverso da qeullo attuale.
*/
window.addEventListener('resize', function() {
    //Questo codice verrà eseguito ogni volta che la finestra viene ridimensionata
    let preAlNav= localStorage.getItem("PrecedenteAltezzaNavbar");
    let alNav= localStorage.setItem("AltezzaNavbar", navbar.offsetHeight);

    /*rendo la navbar responsive impostando la sua larghezza, ad ogni resize della pagina web,
    uguale alla larghezza dello swiper. Faccio ciò a causa di position:fixed
    che ho applicato alla navbar che gli attribuisce una larghezza maggiore rispetto 
    alla larghezza della pagina web.*/
    //console.log(mioSwiper.offsetWidth);
    let l= String(mioSwiper.offsetWidth);
    barraNavigazione.style.width= l + "px";
    
    
    if(preAlNav != alNav){
        console.log("SI");
        localStorage.setItem("PrecedenteAltezzaNavbar", navbar.offsetHeight);
        let altezza= String(navbar.offsetHeight)
        let c= mioSwiper.style.marginTop= altezza + "px";
        //console.log(navbar.offsetHeight);
        //console.log(c);     
    }


    /* ad ogni resize della pagina verifica la larghezza della pagina. Se è superiore a
    992px inserisce un certo testo nel pulsante della navbar, se è inferiore inserisce 
    il testo di default. */
    if(window.innerWidth >= 992){
        console.log(window.innerWidth);
        bottoneStarted.textContent= "Get Started";
    }
    else{
        bottoneStarted.textContent= "Search";
    }


});









/* Restituisce l'ltezza della navbar */
console.log(navbar.offsetHeight);

/* Altezza dell'immagine dello swiper */
console.log(imgSwiper.offsetHeight);

/* Altezza del paragrafo dello swiper */
console.log(pSwiper.offsetHeight);

/* Altezza del h1 dello swiper*/
console.log(h1Swiper.offsetHeight);

/* Altezza del button dello swiper*/
console.log(buttonSwiper.offsetHeight);


/* Al click sull'icona hamburger della navbar
aggiungo del margine allo swiper sotto per 
far vedere il menu a tendina della navbar*/
hamburger.addEventListener('click', () => {
    //console.log(navbar.offsetHeight);
    let altezza= String(navbar.offsetHeight)
    mioSwiper.style.marginTop= altezza + "px";
});


/* Al click sulla voce 'Dropdown' del menù a tendina
della navbar, aggiungo ulteriore margine per dare ulteriore
distacco dallo swiper sottostante (per non far sovrapporre
navbar e swiper)*/
dropdown.addEventListener('click', () => {
    //console.log(navbar.offsetHeight);
    let altezza= String(navbar.offsetHeight)
    mioSwiper.style.marginTop= altezza + "px";
});




/* premendo sulla freccia presente nella sezione copyright, la pagina scrollerà
ogni 1 millisecondo verso l'altro fino a raggiungere l'inizio della pagina.*/
function arrowSquare() {
    frecciaQuadrato.addEventListener('click', e => {
        const altezzaBody = document.body.scrollHeight; //ottengo l'altezza di tutta la pagina html
        const larghezzaBody = document.body.scrollWidth; //ottengo la larghezza di tutta la pagina html
        console.log(altezzaBody, window.innerWidth, larghezzaBody);
            
        let asseX= larghezzaBody;
        let asseY= altezzaBody;
        //console.log(asseX, asseY);

        const timer= setInterval(() => {
            /*scrollTo() è un metodo per scrollare la pagina a una certa posizione (asse x, asse y)*/
            scrollTo(asseX, asseY);
            //console.log(asseX, asseY);

            if(asseY <= 0){
                clearInterval(timer); //ferma il setInterval()
            }
            else{
                asseX= asseX-20;
                asseY= asseY-20;
            }
        }, 1); //1 millisecondo
    
    });
};


//chiamo la function
arrowSquare();


