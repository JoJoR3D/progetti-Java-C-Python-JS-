
let hamburger= document.querySelector('#hamburger');
let menu= document.querySelector('.menu');
let campoRicerca= document.querySelector('.campo-ricerca');
let form= document.querySelector('form');
let contenitoreFilmRicercato= document.querySelector('.filmRicercato');


//salvo il film ricercato
let arrFilmCercato= [];


//clicco sull'iconda hamburger per far apparire il menu
hamburger.addEventListener('click', () => {

    hamburger.style.display= "none";
    menu.style.display= "flex";
})

//clicco su Search
menu.addEventListener('click', e => {

    //console.log(e);
    
    if(e.target.textContent == "Search"){
        campoRicerca.classList.toggle('show');

        if(campoRicerca.classList.contains('show')){
            contenitoreFilmRicercato.style.display= "none";
            contenitoreFilmRicercato.innerHTML= ""; //pulisco il contenuto
            carosello.style.display= "flex";
        } 
    }
});






//prendo tutti il film che coincide con quello che sto iniziando a scrivere nel campo search
form.addEventListener('keyup', e => {

    e.preventDefault();

    let titoloFilmInserito= form.ricerca.value;

    const url= `http://www.omdbapi.com/?t=${titoloFilmInserito}&apikey=${key}`;

    //richiesta http per recuperare il film inserito dal server
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);

            carosello.style.display= "none";
            contenitoreFilmRicercato.style.display= "flex";

            if(data.Response != 'False')
                updateUI(data, 2);
            else
                contenitoreFilmRicercato.textContent= "Film non trovato";
        })


});








//prendo il titolo del film inserito e lo mostro
// form.addEventListener('submit', e => {

//     e.preventDefault();

//     let titoloFilmInserito= form.ricerca.value;
//     console.log(titoloFilmInserito);
//     form.reset();

//     const url= `http://www.omdbapi.com/?t=${titoloFilmInserito}&apikey=${key}`;

//     //richiesta http per recuperare il film inserito dal server
//     fetch(url)
//         .then(response => response.json())
//         .then(data => {
//             console.log(data);

//             /* carosello.style.display= "none";
//             contenitoreFilmRicercato.style.display= "flex"; */

//             if(data.Response != 'False')
//                 updateUI(data, 2);
//             else
//                 contenitoreFilmRicercato.textContent= "Film non trovato";
//         })
// });
