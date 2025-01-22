
const key= "25ca6804";


let titoloFilm= ["Iron Man ", "Eternals", "Spider-Man: Homecoming", "Black Widow", "Thor: Love and Thunder", "Black Panther: Wakanda Forever", "Deadpool & Wolverine", "Avengers: Infinity War", "Avengers: Endgame"];


let carosello= document.querySelector(".carosello");
let schedeFilm= document.querySelector(".schedeFilm");
let filmRicercato= document.querySelector(".filmRicercato")

let i= 0;
let j= 0;
let contCard= 0;
let contClick= 0;
let cont= 0;
let cont2= 0;

//array che conterrà tutti i titoli dei film del carosello, in modo da poter poi aggiungerli come nomi delle classi
let arrayFilm= [];

//per assicurarmi di avere sempre 3 carte in ogni schermata del carosello
let aggiornamentoSchede= [0,0,1,2,3];
let aggiornamento= 0;







//click sulle due frecce del carosello
carosello.addEventListener('click', e => {
    //console.log(e);    

    //al click sulla freccia destra del carosello
    if(e.target.classList[1] == "fa-angle-right"){
        console.log(e);

        aggiornamento= aggiornamentoSchede[j];
        ++contClick;
        //console.log("destra:",contClick, i, cont);

        if(contClick < 7){

            while(i < titoloFilm.length && aggiornamento == aggiornamentoSchede[j]){
                let titolo= titoloFilm[i];
                
                riempiCarosello(titolo)
                    .then(data => {
                        //console.log(data);
                        //elimino gli spazi al titolo per aggiungerlo come classe
                        let titoloSenzaSpazi= deleteSpace(data.Title);
                        //console.log(titoloSenzaSpazi);

                        scor(cont, "none");        

                        //se il film è già presente nel carosello
                        if(!(arrayFilm.includes(titoloSenzaSpazi))){
                            updateUI(data, 1);
                        }
                        //altrimenti
                        else{
                            scor(cont + 3, "block");  
                        }

                        cont++;
                        cont2= cont-1;

                    })
                    .catch(err => {
                        console.log(err);
                    });
                            
                i++;
                aggiornamento++;
            }
            j++;
            contCard++;
        }
        
        //arrivato alla fine del carosello (cliccando la freccia di destra), ricomincio dall'inizio
        else{
            contCard= 0;
                        
            scor(cont, "none"); 
            scor(contCard, "block"); 
            //prende il primo film e lo mette all'ultimo posto della lista
            scambioCard(contCard);            
        }
    }

    //al click sulla freccia sinistra del carosello
    else if(e.target.classList[1] == "fa-angle-left"){
        console.log(e);

        //qui se non è avvenuto nessuno "swap" (metodi append e prepend) dei film
        if(contCard > 0){
            if(cont2 > 0){
                scor(cont2, "block");
                scor(cont+2, "none");
                cont2--;
                cont--;
            }
            else if(cont2 == 0){
                if(i > 3){
                    scor(cont2, "block");
                    scor(cont+2, "none");
                    cont2--;
                }
                contClick= 0;
                i= 3;
                j= 0;
                cont= 0;
            }
        }
        
        //qui quando sono avvenuti degli swap
        else{
            scor(cont-1, "block"); 
            scor(cont+2, "none"); 
            //prende il primo film e lo mette all'ultimo posto della lista
            scambioCard2(cont+2);
        }
    }


    aggiornamento= 0;
})



//scorrendo verso destra, arrivati alla fine del carosello
//tolgo il primo film del carosello e lo inserisco all'ultim aposizione del carosello. Così con i successivi.
function scambioCard(x){

    let a= schedeFilm.children[x];
    
    a.remove();    
    schedeFilm.appendChild(a);
}


//scorrendo verso sinistra, rimuovo l'ultimo film (elemento div) e lo metto come primo elemento nel carosello.
function scambioCard2(x){

    let a= schedeFilm.children[x];
    a.remove();
    schedeFilm.prepend(a);
}






//chiamata http tramite function API fetch
let riempiCarosello= async (titolo) => {

    const url= `http://www.omdbapi.com/?t=${titolo}&apikey=${key}`;
      
    let response= await fetch(url);

    if(response.status !== 200){
        throw new Error("Non è stato possibile ottenere i dati richiesti");
    }
    
    let data= await response.json();
    
    return data;
};





/* PER AVVIO  e SCORRIMENTO CAROSELLO*/

let updateUI= (data, valore) => {

    //elimino gli spazi al titolo per aggiungerlo come classe
    let titoloSenzaSpazi= deleteSpace(data.Title);
    //console.log(titoloSenzaSpazi);

    //creo un array contenente gli attori
    let listaAttori= data.Actors.split(',');

    let schedaFilm= `
        <div class="${titoloSenzaSpazi} scheda-film">
            
            <div class="div-titolo-film-carosello show">
                <h2 class="titolo-film-carosello"><a href="./dettagliFilm.html" target="_blank">${data.Title}</a></h2>
            </div>
            
            <div class="div-img-carosello">
                <img id="img-carosello" src="${data.Poster}" 
                alt="locandina film">
            </div>
            <br>
            <div class="paragrafo-carosello show">
                <div class="attori">
                    <p>Attori:</p>
                    <a href="https://it.wikipedia.org/wiki/${listaAttori[0]}" target="_blank">${listaAttori[0]}</a>
                    <a href="https://it.wikipedia.org/wiki/${listaAttori[1]}" target="_blank">${listaAttori[1]}</a>
                    <a href="https://it.wikipedia.org/wiki/${listaAttori[2]}" target="_blank">${listaAttori[2]}</a>
                </div>
                <br>
                <p>Generi:</p>
                <p class="generi">${data.Genre}</p>
            </div>
            <p>Anno uscita:</p>
            <p class="anno-uscita">${data.Released}</p>
            <br>
            <p>Durata:</p>
            <p class="durata-film">${data.Runtime}</p>
        </div>
    `;


    //per inserire i film nel carosello
    if(valore == 1)
        schedeFilm.innerHTML += schedaFilm;
    //per quanto ricerco un film (devo sovrascrivere il precedente)
    else if(valore == 2)
        filmRicercato.innerHTML= schedaFilm;


    arrayFilm.push(titoloSenzaSpazi);  
};



//function che applica display none ai film precedenti
let scor= (val, proprieta) => {
    //console.log(schedeFilm.children[val]);
    
    schedeFilm.children[val].style.display= proprieta;
}



//ad avvio pagina web aggiungo i primi 3 film al carosello
while(i < 3){
    let titolo= titoloFilm[i];
    riempiCarosello(titolo)
        .then(data => {
            //console.log(data);

            updateUI(data, 1);
                        
        })
        .catch(err => {
            console.log(err);
        });
    
    i++;
    contCard= 3;
};




//function per eliminare gli spazi
function deleteSpace(stringa){

    let s= "";

    for(let j=0; j < stringa.length; j++){
        if(stringa[j] == ' ' || stringa[j] == ':'){
            if(s[j-1] != '-')
                s += '-';
        }
        else
            s += stringa[j];
    }

    return s;
}