
const navbar= document.querySelector('.navbar');
const carrello= document.querySelector('.carrello');
const chiudiElencoBrani= document.querySelector('.chiudi-elenco-brani');
const logo= document.querySelector('.logo');
const textInput= document.querySelectorAll('.text-input');




/*Altezza della navbar*/
/*imposto in automatico il margin top che divide la sezione carrello
dalla navbar sia al primo avvio della pagina web e sia con eventuali 
resize della pagina web*/
console.log(navbar.offsetHeight);
let stringa= String(navbar.offsetHeight + 50);
carrello.style.top= stringa + "px";


window.addEventListener('resize', () =>{
    let stringa= String(navbar.offsetHeight + 50);
    carrello.style.top= stringa + "px";

    /*per ridimensionare il font size del campo input quantità album ad ogni resize*/
    textInput.forEach(element => {
        if(navbar.offsetWidth >= 992 && navbar.offsetWidth < 1150){
            let s= 0.75 + 'rem';
            element.style.fontSize= s;
        }
        else{
            let s= 1 + 'rem';
            element.style.fontSize= s; 
        }
    });
});


/*per ridimensionare il font size del campo input quantità album all'avvio*/
textInput.forEach(element => {
    if(navbar.offsetWidth >= 992 && navbar.offsetWidth < 1150){
        let s= 0.75 + 'rem';
        element.style.fontSize= s;
    }
});










/*per far apparire la 'x' che consente di chiudere la sezione ricerca
artista. Questa 'x' apparirà solo se il width della pagina web è maggiore
a 992px*/
function contollaWidthNavbar(){
    tendinaChiusa.style.display= "none";
    tendinaAperta.style.display= "inline";

    /*let larghezza= 300 + 'px';
    let altezza= 200 + 'px';
    logo.style.width= larghezza;
    logo.style.height= altezza;*/
    

    //eventi di click
    tendinaChiusa.addEventListener('click', () => {
        chiudiElencoBrani.style.display= "inline";
        tendinaAperta.style.display= "inline";
        tendinaChiusa.style.display= "none";

        /*let larghezza= 300 + 'px';
        let altezza= 200 + 'px';
        logo.style.width= larghezza;
        logo.style.height= altezza;*/
    });

    tendinaAperta.addEventListener('click', () => {
        chiudiElencoBrani.style.display= "none";
        tendinaAperta.style.display= "none";
        tendinaChiusa.style.display= "inline";

        /*let larghezza= 150 + 'px';
        let altezza= 100 + 'px';
        logo.style.width= larghezza;
        logo.style.height= altezza;*/
    });
}








/************************************************************************/

const formSearch= document.querySelector('.form-search');
const inserBrani= document.querySelector('.inser-brani');
const peb= document.querySelector('.peb');
const inserAlbum= document.querySelector('.inser-album');
const tendinaAperta= document.querySelector('.tendina-aperta');
const tendinaChiusa= document.querySelector('.tendina-chiusa');

/*evento che al submit prende l'artista inserito dall'utente e ne ricerca i brani*/
formSearch.addEventListener('submit', e => {

    e.preventDefault();

    let artista= (formSearch.inputSearch.value);

    //pulisco il campo
    formSearch.inputSearch.value= "";

    musica(artista)
        .catch(e => {
            console.log(e.message);
        });
});



/*richiesta api per cercare un'artista e ottenere i suoi album*/
async function musica(artista){

    let response=  await fetch(`https://deezerdevs-deezer.p.rapidapi.com/search?q=${artista}`, {
        method: "GET",
        headers: {'x-rapidapi-key': '8135c8ef44mshf9e4f575f6a7395p17fe26jsncf195e669163', 'x-rapidapi-host': 'deezerdevs-deezer.p.rapidapi.com',
        "Content-Type": "application/json"
        },
    });

    //console.log(response.status);
    
    let data= await response.json();
    console.log(data);

    stampaBrani(data);
    sceltaAndInserBrano(data);
    contollaWidthNavbar();
}



//function che stampa i brani ottenuti dalla chiamata fetch e li inserisce nella pagina html
function stampaBrani(brani){
    let arrayBrani= brani.data;
    peb.style.display= "block";

    /*pulisco il contenuto del tag ul nel caso in cui dopo aver cercato
    un artista e inserito i suoi brani. L'utente ricerchi un altro artista. In questo modo i brani del precedente artista ricercato verrano tolti dall'ul per fa spazio a brani dell'attuale artista ricercato.*/
    inserBrani.innerHTML = ""; 
   
    arrayBrani.forEach(brano => {
        console.log(brano.title); 

        inserBrani.innerHTML += 
        `<li>${brano.title}</li>`
    });
}



/*evento che permette all'utente di inserire uno dei brani ricercati nel carrello*/
function sceltaAndInserBrano(album){
    inserBrani.addEventListener('click', e => {
        console.log(e.target.textContent);

        let arrayAlbum= album.data;
        let img= "";
        let artista= "";
        let id= "";
        let permesso= false;

        arrayAlbum.forEach(el => {
            //console.log(el.title);
            
            if(el.title == e.target.textContent){
                console.log("dentro");
                
                /*una volta che l'utente ha scelto il brano da inserire nel carrello, questo viene selezionato (colore blu) e non può essere inserito nuovamente*/
                if(e.target.style.color == 'blue'){
                    permesso;
                }
                else{
                    e.target.style.color= 'blue';
                    permesso= true;
                }

                img= el.album.cover_medium;
                artista= el.artist.name;
                id= el.id;
            }
        });
        console.log("fuori");

        /*inserisco il nuovo album nel carrello se non è già presente*/
        if(permesso == true){
            const frammento = document.createDocumentFragment();
            const nuovoAlbum= document.createElement('div');
            nuovoAlbum.innerHTML=
                `<div class="row mb-3">
                    <div class="col-12 col-lg-3">
                        <img src=${img} alt="copertina dell' album the new Abnormal del gruppo the strokes" class="copertina" style="max-width: 100%; width: 100%;">
                    </div>
                    <div class="col-6 col-lg-3 mt-4">
                        <p class="mb-0" style="color:rgb(255,255,255,0.55)">Vinile</p>
                        <p class="mb-0"><strong>${artista}</strong></p>
                    </div>
                    <div class="col-6 col-lg-3 mt-4 inserForm-${id}">
                            
                    </div>
                    <div class="col-12 col-lg-3 mt-lg-4 dustbin evento-dustbin-${id} ">
                        <strong>€ 20.00</strong>
                        
                    </div>

                    <div class="cont-linea mt-3">
                        <div class="linea"></div>
                    </div>

                </div>`;
            
            /*lo inserisco nella pagina html*/
            frammento.appendChild(nuovoAlbum)
            inserAlbum.appendChild(frammento); 


            /*poi nel nuovo album aggiunto gli inserisco il form sul quale aggiungere l'evento*/
            let s= '.inserForm-' + id;
            const inserForm= document.querySelector(s);
            const frammento2 = document.createDocumentFragment();
            const nuovoForm= document.createElement('form');
            nuovoForm.classList.add('form', 'd-flex', 'flex-row');

            nuovoForm.innerHTML=
                `
                    <i class="bi bi-plus segno-piu me-1"></i>
                    <input type="text" name="quantitalbum" placeholder="inserisci quantità" class="text-input" style="width: 100%; height: 32px; max-height: 32px; max-width: 135px; border: 0px solid white; border-radius: 3px;">
                    <i class="bi bi-dash segno-meno ms-1"></i>
                `;
            


            /*poi nel nuovo album aggiunto gli inserisco il tag i contenente il cestino che consente di eliminare l'album dal carrello*/
            s= '.evento-dustbin-' + id;
            const inserCestino= document.querySelector(s);
            const frammento3 = document.createDocumentFragment();
            const nuovoCestino= document.createElement('i');
            nuovoCestino.classList.add('bi', 'bi-trash3', 'cestino');

            /*evento che consente di eliminare l'album dal carrello cliccando sul cestino*/
            eliminaAlbumAggiuntoDaCarrello(nuovoCestino);

            /*lo inserisco nella pagina html*/
            frammento3.appendChild(nuovoCestino);
            inserCestino.appendChild(frammento3); 



            /*evento (sul form) sul nuovo album aggiunto per incrementarne o diminuirne la quantità*/
            nuovoForm.addEventListener('click', e => {
                //console.log(e);
                e.preventDefault();

                let flag= 1
                    
                //se si clicca sul segno piu
                if(e.target.classList[2] == "segno-piu"){
                    //se il campo input è vuoto, gli metto 1
                    if(nuovoForm.quantitalbum.value === ""){
                        let valNumerico= 0;
                        valNumerico++;
                        nuovoForm.quantitalbum.value= String(valNumerico);
            
                        /*aggiorno la quantità nel carrello*/
                        contOggettiNelCarrello= contOggetti(nuovoForm, flag);
                        numOggetti.style.display= 'inline';
                        numOggetti.textContent= contOggettiNelCarrello;
                    }
                    //incremento il valore presente nel campo input
                    else{
                        //console.log(el.quantitalbum.value);
                        let valNumerico= parseInt(nuovoForm.quantitalbum.value);
                        valNumerico++;
                        //console.log(valNumerico);
                        nuovoForm.quantitalbum.value= String(valNumerico);
            
                        /*aggiorno la quantità nel carrello*/
                        contOggettiNelCarrello= contOggetti(nuovoForm, flag);
                        numOggetti.style.display= 'inline';
                        numOggetti.textContent= contOggettiNelCarrello;
                    }
                }
            
                //se si clicca sul segno meno
                else if(e.target.classList[2] == "segno-meno"){
                    //decremento il valore presente nel campo input solo se è > di 0
                    if(nuovoForm.quantitalbum.value > 0){
                        let valNumerico= parseInt(nuovoForm.quantitalbum.value);
                        //console.log(form.quantitalbum.value);
                        valNumerico--;
                        //console.log(valNumerico);
                        nuovoForm.quantitalbum.value= String(valNumerico);
            
                        flag= 2
            
                        /*aggiorno la quantità nel carrello*/
                        contOggettiNelCarrello= contOggetti(nuovoForm, flag);
                        numOggetti.style.display= 'inline';
                        numOggetti.textContent= contOggettiNelCarrello;
                    }
                }

                //prezzo album per quantità
                let parso= getPrezzo(e, flag);
                let prezzoPerNumOggetti= parso * contOggettiNelCarrello;
                //aggiorno il prezzo complessivo nella sezione riepilogo ordine
                putPrezzo.textContent= '€ ' + String(prezzoPerNumOggetti) + '.00';

                //aggiorno il prezzo totale da pagare
                let costoSpedizione= estrazioneCostoSpedizione(btn);
                prezzoTotale.textContent= '€ ' + (prezzoPerNumOggetti + costoSpedizione) + '.00';
            });
            

            /*se l'utente inserisce a mano una quantità di album da voler aggiungere al carrello, all'invio verranno incrementiti il numero
            di oggetti nel carrello*/
            nuovoForm.addEventListener('submit', e => {
                e.preventDefault();
            
                let flag= 3;
            
                contOggettiNelCarrello= contOggetti(nuovoForm, flag);
                numOggetti.style.display= 'inline';
                numOggetti.textContent= contOggettiNelCarrello;

                //prezzo album per quantità
                let prezzoPerNumOggetti= parso * contOggettiNelCarrello;
                //aggiorno il prezzo complessivo nella sezione riepilogo ordine
                putPrezzo.textContent= '€ ' + String(prezzoPerNumOggetti) + '.00';

                //aggiorno il prezzo totale da pagare
                let costoSpedizione= estrazioneCostoSpedizione(btn);
                prezzoTotale.textContent= '€ ' + (prezzoPerNumOggetti + costoSpedizione) + '.00';
            });
                

            /*lo inserisco nella pagina html*/
            frammento2.appendChild(nuovoForm);
            inserForm.appendChild(frammento2); 
        }

        else{
            console.log("Album già presente nel carrello");
        }
    });
};












/************************************************************************/

/*per inserire quante copie di un album si desidera acquistare e ne salva 
in una variabile (contOggettiNelCarrello) il numero di oggwetti totali*/

const form= document.querySelectorAll('.form');
const numOggetti= document.querySelector('.num-oggetti');
const putPrezzo= document.querySelector('.putPrezzo');
const prezzoTotale= document.querySelector('.prezzo-totale');
const btn= document.querySelector('.btn-spedizione');

let contOggettiNelCarrello= 0;


form.forEach(el => {    

    el.addEventListener('click', e => {
        //console.log(e);     

        e.preventDefault();

        let flag= 1
        
        //se si clicca sul segno piu
        if(e.target.classList[2] == "segno-piu"){
            //se il campo input è vuoto, gli metto 1
            if(el.quantitalbum.value === ""){
                let valNumerico= 0;
                valNumerico++;
                el.quantitalbum.value= String(valNumerico);

                /*aggiorno la quantità nel carrello*/
                contOggettiNelCarrello= contOggetti(el, flag);
                numOggetti.style.display= 'inline';
                numOggetti.textContent= contOggettiNelCarrello;
            }
            //incremento il valore presente nel campo input
            else{
                //console.log(el.quantitalbum.value);
                let valNumerico= parseInt(el.quantitalbum.value);
                valNumerico++;
                //console.log(valNumerico);
                el.quantitalbum.value= String(valNumerico);

                /*aggiorno la quantità nel carrello*/
                contOggettiNelCarrello= contOggetti(el, flag);
                numOggetti.style.display= 'inline';
                numOggetti.textContent= contOggettiNelCarrello;
            }
        }

        //se si clicca sul segno meno
        else if(e.target.classList[2] == "segno-meno"){
            //decremento il valore presente nel campo input solo se è > di 0
            if(el.quantitalbum.value > 0){
                let valNumerico= parseInt(el.quantitalbum.value);
                //console.log(form.quantitalbum.value);
                valNumerico--;
                //console.log(valNumerico);
                el.quantitalbum.value= String(valNumerico);

                flag= 2

                /*aggiorno la quantità nel carrello*/
                contOggettiNelCarrello= contOggetti(el, flag);
                numOggetti.style.display= 'inline';
                numOggetti.textContent= contOggettiNelCarrello;
            }
        }

        //prezzo album per quantità
        let parso= getPrezzo(e, flag);
        let prezzoPerNumOggetti= parso * contOggettiNelCarrello;
        //aggiorno il prezzo complessivo nella sezione riepilogo ordine
        putPrezzo.textContent= '€ ' + String(prezzoPerNumOggetti) + '.00';

        //aggiorno il prezzo totale da pagare
        let costoSpedizione= estrazioneCostoSpedizione(btn);
        prezzoTotale.textContent= '€ ' + (prezzoPerNumOggetti + costoSpedizione) + '.00';
    });

    /*se l'utente inserisce a mano una quantità di album da voler aggiungere al carrello, all'invio verranno incrementiti il numero
    di oggetti nel carrello*/
    el.addEventListener('submit', e => {
        e.preventDefault();

        let flag= 3;
        let parso= getPrezzo(e, flag);

        contOggettiNelCarrello= contOggetti(el, flag);
        numOggetti.style.display= 'inline';
        numOggetti.textContent= contOggettiNelCarrello;

        //prezzo album per quantità
        let prezzoPerNumOggetti= parso * contOggettiNelCarrello;
        //aggiorno il prezzo complessivo nella sezione riepilogo ordine
        putPrezzo.textContent= '€ ' + String(prezzoPerNumOggetti) + '.00';

        //aggiorno il prezzo totale da pagare
        let costoSpedizione= estrazioneCostoSpedizione(btn);
        prezzoTotale.textContent= '€ ' + (prezzoPerNumOggetti + costoSpedizione) + '.00';
    });

});



/*function che aggiorna la quantità nel carrello*/
function contOggetti(elemento, flag){
    let numero= parseInt(elemento.quantitalbum.value);
    //console.log(elemento.quantitalbum.value, numero);
    
    /*inserisce le copie incrementandole il segno più*/
    if(flag == 1){
        contOggettiNelCarrello++;
    }
    /*decrementa il numero di copie da acquistare premendo sul segno meno*/
    else if(flag == 2){
        contOggettiNelCarrello--;
    }
    /*inserisce le copie manualmente*/
    else if(flag == 3){
        contOggettiNelCarrello= contOggettiNelCarrello + numero;
    }
    
    return contOggettiNelCarrello;
}















/************************************************************************/

/*prendo il prezzo di ogni album*/

function getPrezzo(e, flag){
    //ricavo il prezzo dell'album
    //console.log(e.target.parentNode.parentNode.nextElementSibling.children[0].textContent);
    //console.log(e.target.parentNode.nextElementSibling.children[0].textContent);
    let prezzo= 0
    
    if(flag == 1 || flag == 2){
        prezzo= e.target.parentNode.parentNode.nextElementSibling.children[0].textContent;
    }
    else if(flag == 3){
        prezzo= e.target.parentNode.nextElementSibling.children[0].textContent;
    }      

    //prezzo = € 20.00
    let separa= prezzo.split(' ');
    //prendoPrezzo= 20
    let prendoPrezzo= separa[1];
    //lo parso in un intero
    let parso= parseInt(prendoPrezzo);

    return parso;
}














/************************************************************************/

/*scelta del tipo di spedizione*/

const ulMenuSpedizione= document.querySelector('.ul-menu-spedizione');

ulMenuSpedizione.addEventListener('click', e => {
    //spedizione che si è selezionata
    //console.log(e.target.textContent);
    let choiceShipping= e.target.textContent;

    //spedizione attualmente impostata
    //console.log(e.target.parentNode.previousElementSibling.innerText);
    let shipping= e.target.parentNode.previousElementSibling.innerText;

    //imposto la spedizione scelta come quella da impostare   
    e.target.parentNode.previousElementSibling.innerText= choiceShipping;
    e.target.textContent= shipping;


    //AGGIORNO il costo della spedizione nel prezzo totale
    //sottraggo dal prezzo totale la spedizione standard presente di default
    //contenuto contiene la stringa: Spedizione standard- € 5.00
    let contenuto= shipping.trim();
    let splitto= contenuto.split(' ');
    let costoSpedizione= parseInt(splitto[3]);
    let splitPrezzoTotale= prezzoTotale.textContent.split(' ');
    let number= parseInt(splitPrezzoTotale[1]);  
    number -= costoSpedizione; 
    
    //aggiungo al prezzo totale il costo della spedizione selezionata dall'utente
    contenuto= choiceShipping.trim();
    splitto= contenuto.split(' ');
    costoSpedizione= parseInt(splitto[3]);
    number += costoSpedizione;
    prezzoTotale.textContent= '€ ' + number + '.00';  
});




//function per ottenere dalla stringa spedizione (es: Spedizione standard- € 5.00) solo il costo

function estrazioneCostoSpedizione(btn){
    //contenuto contiene la stringa: Spedizione standard- € 5.00
    let contenuto= btn.textContent.trim();
    let splitto= contenuto.split(' ');
    let costoSpedizione= parseInt(splitto[3]);

    return costoSpedizione;
}
















/************************************************************************/

/*questa function elimina l'album dal carrello una volta cliccato sull'
icona del cestino*/

const cestino= document.querySelectorAll('.cestino');

function eliminaAlbumDaCarrello(){

    cestino.forEach(cest => {
        cest.addEventListener('click', e => {
            /*prima di eliminare l'album dal carrello, controllo che non ci 
            siano copie nel campo input e che quindi queste copie non siano
            state aggiunte al prezzo. Se si allora devo anche decrementare queste copie dell'album dal prezzo e al prezzo totale*/
            let campoInputCopie= e.target.parentNode.previousElementSibling.children[0].children[1].value;       
    
            if(campoInputCopie != ""){
                let num= parseInt(campoInputCopie);
                let prezzoAlbum= e.target.previousElementSibling.textContent;
                let separa= prezzoAlbum.split(' ');
                let prendoPrezzo= separa[1];
                let numCopiePerPrezzo= num*prendoPrezzo;
               
                //es: prezzo = € 20.00
                separa= putPrezzo.textContent.split(' ');
                //prendoPrezzo= 20
                prendoPrezzo= separa[1];
                //lo parso in un intero
                let parsoPrezzo= parseInt(prendoPrezzo);
    
                //es: prezzo = € 20.00
                separa= prezzoTotale.textContent.split(' ');
                //prendoPrezzo= 20
                prendoPrezzo= separa[1];
                //lo parso in un intero
                let parsoPrezzoTot= parseInt(prendoPrezzo);
    
                parsoPrezzo -= numCopiePerPrezzo;
                parsoPrezzoTot -= numCopiePerPrezzo;
                putPrezzo.textContent= '€ ' + parsoPrezzo + '.00';
                prezzoTotale.textContent= '€ ' + parsoPrezzoTot + '.00'; 
    
                //diminuisco il numero di oggetti nel carrello
                numOggetti.textContent -= num;
                contOggettiNelCarrello -= num;
            }
                            
    
            //risalgo al div che contiene l'album da eliminare dal carrello
            //console.log(e.target.parentNode.parentNode);
            let album= e.target.parentNode.parentNode;
            album.remove();       
        });
    });
}


eliminaAlbumDaCarrello();













/************************************************************************/
/*Evento per gli album aggiunti cercando un'artista tramite la fetch*/

/*questa function elimina l'album dal carrello una volta cliccato sull'
icona del cestino*/


function eliminaAlbumAggiuntoDaCarrello(nuovoCestino){

    nuovoCestino.addEventListener('click', e => {
            //console.log(e);
            
            /*prima di eliminare l'album dal carrello, controllo che non ci 
            siano copie nel campo input e che quindi queste copie non siano
            state aggiunte al prezzo. Se si allora devo anche decrementare queste copie dell'album dal prezzo e al prezzo totale*/
            let campoInputCopie= e.target.parentNode.previousElementSibling.children[0].children[1].value;       
    
            if(campoInputCopie != ""){
                let num= parseInt(campoInputCopie);
                let prezzoAlbum= e.target.previousElementSibling.textContent;
                let separa= prezzoAlbum.split(' ');
                let prendoPrezzo= separa[1];
                let numCopiePerPrezzo= num*prendoPrezzo;
               
                //es: prezzo = € 20.00
                separa= putPrezzo.textContent.split(' ');
                //prendoPrezzo= 20
                prendoPrezzo= separa[1];
                //lo parso in un intero
                let parsoPrezzo= parseInt(prendoPrezzo);
    
                //es: prezzo = € 20.00
                separa= prezzoTotale.textContent.split(' ');
                //prendoPrezzo= 20
                prendoPrezzo= separa[1];
                //lo parso in un intero
                let parsoPrezzoTot= parseInt(prendoPrezzo);
    
                parsoPrezzo -= numCopiePerPrezzo;
                parsoPrezzoTot -= numCopiePerPrezzo;
                putPrezzo.textContent= '€ ' + parsoPrezzo + '.00';
                prezzoTotale.textContent= '€ ' + parsoPrezzoTot + '.00'; 
    
                //diminuisco il numero di oggetti nel carrello
                numOggetti.textContent -= num;
                contOggettiNelCarrello -= num;
            }
                            
    
            //risalgo al div che contiene l'album da eliminare dal carrello
            //console.log(e.target.parentNode.parentNode);
            let album= e.target.parentNode.parentNode;
            album.remove();       
        });
}