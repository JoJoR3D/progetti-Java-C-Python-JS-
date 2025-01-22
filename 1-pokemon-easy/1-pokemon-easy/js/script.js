const pokemons = [{
    id: 0,
    nome: "Bulbasaur",
    tipo: "erba",
    abilita: "Foglielama",
    sprite: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
    spriteSpalle: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
    info: "Il best boy. Abbastanza socievole se non infastidito"
}, {
    id: 1,
    nome: "Charmander",
    tipo: "fuoco",
    abilita: "Braciere",
    sprite: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
    spriteSpalle: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/4.png",
    info: "In caso vada fuori controllo chiamare 112 e farsi passare i pompieri"
}, {
    id: 2,
    nome: "Squirtle",
    tipo: "acqua",
    abilita: "pistolacqua",
    sprite: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
    spriteSpalle: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/7.png",
    info: "Non è un pompiere"
}, {
    id: 3,
    nome: "Pikachu",
    tipo: "elettrico",
    abilita: "tuonoshock",
    sprite: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    spriteSpalle: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
    info: "Coloro i quali lo agganceranno al contatore saranno punibili secondo norma cod. Penale"
}];



/*seleziono il main*/
const contenitoreP = document.querySelector("main");

/*ciclo sull'array di oggetti per prendere ogni oggetto e inserirlo nella
pagina html (inseriamo ogni carta in un div con id= pokemon.id). 
Assegno tutto ad una variabile (templateCard) che poi
inserisco nella html*/
pokemons.forEach((pokemon) => {
  let templateCard = `
    <div id= "${pokemon.id}" class="pokemon-card"> 
        <img class="img" src="${pokemon.sprite}" alt="${pokemon.nome}">
        <h2 class="nomeP">${pokemon.nome}</h2>
        <p class= "abilita"> Abilita: ${pokemon.abilita}</p>
        <p class="info">${pokemon.info}</p>
        <button class="btn"> Mostra Info </button>
    </div>`

  contenitoreP.innerHTML += templateCard;
});



/*seleziono tutti i bottoni*/
const bottoni = document.querySelectorAll(".btn");

/*creo un addEventListener sul main, cioè ascolto ogni 'click'
che l'utente fa nel main, ma l'evento parte solo quando l'utente
clicca su uno dei button presenti nel main*/
contenitoreP.addEventListener("click", e => {
  console.log(e);

  /*se l'utente clicca su un bottone*/
  if (e.target.tagName === "BUTTON") {
    console.log(e);
    
    console.log(e.target.previousElementSibling);

    /*prendo l'elemento html precedente (previousElementSibling) al bottone
    che nel nostro caso è il tag <p> con classe "info" egli aggiungo la classe
    "mostra" (questa classe disattiva il display none presente nella classe info
    per mettere display "block" (cioè facciamo apparire il tag <p>) (display
    block indica un comportamento predefinito (statico). Display flex (dinamico))*/
    e.target.previousElementSibling.classList.toggle("mostra");

    /*se il pulsante contiene il testo "Nascondi info", vuol dire che è già stato
    premuto, quindi ripremendolo, gli inseriamo il testo "Mostra info", e dal elemento padre (parentElement)
    del bottone (e.target) che è il div, prendo il primo figlio del div (firstElementChild) che
    è il tag <img> e setto l'attributo src del tag img (src contiene il link/percorso della 
    immagine), passandogli sprite che contiene il link dell'immagine non girata di spalle. Come?
    Prenod pokemons che è l'array di oggetti e gli passo come indice tra le [] il padre (parentElement)
    del bottone premuto (e.target) che è il div che contiene la classe e mi prendo l'attributo id 
    (getAttribute("id") se clicco la prima carta l'attributo id sarà 0).
    Poi dell'oggetto mi vado a prende sprtireSpalle che contiene il link 
    dell'immagine del pokemon girato di spalle.
    
    L'else fa l'opposto. Se il bottone contiene il testo "Mostra info", vuol dire che
    non p stato ancora premuto, quindi premendolo vado a cambiare il testo del bottone
    e ad inserire nell'attributo src del tag img .sprite dell'array di oggetti che contiene
    il link dell'immagine del pokemon girato di spalle.*/
    if (e.target.textContent === "Nascondi Info") {
      e.target.textContent = "Mostra Info";
      e.target.parentElement.firstElementChild.setAttribute(
        "src",
        pokemons[e.target.parentElement.getAttribute("id")].sprite
      );
    } else {
      e.target.textContent = "Nascondi Info";
      e.target.parentElement.firstElementChild.setAttribute(
        "src",
        pokemons[e.target.parentElement.getAttribute("id")].spriteSpalle
      );
    }
  }
});
