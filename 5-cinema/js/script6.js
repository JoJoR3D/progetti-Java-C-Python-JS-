
let main= document.querySelector('main');

//carosello film
const nome = localStorage.getItem("nome");

//film ricercato
const nomeSearch= localStorage.getItem("nomeSearch");

console.log(nomeSearch);
console.log(nome);



const key= "25ca6804";



let dettagliFilm= async (titolo) => {

    const url= `http://www.omdbapi.com/?t=${titolo}&apikey=${key}`;
      
    let response= await fetch(url);

    if(response.status !== 200){
        throw new Error("Non è stato possibile ottenere i dati richiesti");
    }

    let data= await response.json();
    
    return data;
};


if(nome != ""){
    dettagliFilm(nome)
        .then(data => {
            console.log(data);
            costruzione(data);
            localStorage.setItem("nome", "");
            localStorage.setItem("nomeSearch", "");
        })
        .catch(err => {
            console.log(err);
        })
}


if(nomeSearch != ""){
    dettagliFilm(nomeSearch)
        .then(data => {
            console.log(data);
            costruzione(data);
            localStorage.setItem("nome", "");
            localStorage.setItem("nomeSearch", "");
        })
        .catch(err => {
            console.log(err);
        })
}




function costruzione(data){

    //creo un array contenente gli attori
    let listaAttori= data.Actors.split(',');

    let schedaFilm= `
        <div class="scheda-film">
            
            <div class="div-titolo-film-carosello">
                <h2 class="titolo-film-carosello"><a href="https://it.wikipedia.org/wiki/${data.Title}" target="_blank">${data.Title}</a></h2>
            </div>
            
            <div class="div-img-carosello">
                <img id="img-carosello" src="${data.Poster}" 
                alt="locandina film">
            </div>
            <br>
            <div class="paragrafo-carosello">
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
            <br>
            <p>Anno uscita:</p>
            <p class="anno-uscita">${data.Released}</p>
            <br>
            <p>Durata:</p>
            <p class="durata-film">${data.Runtime}</p>
            <br>
            <p>Regista:</p>
            <p class="regista">${data.Director}</p>
            <br>
            <p>Scrittori:</p>
            <p class="scrittori">${data.Writer}</p>
            <br>
            <p>Plot:</p>
            <p class="plot">${data.Plot}</p>
            <br>
            <p>Lingua:</p>
            <p class="lingua">${data.Language}</p>
            <br>
            <p>Paese:</p>
            <p class="paese">${data.Country}</p>
            <br>
            <p>Awards:</p>
            <p class="awards">${data.Awards}</p>
            <br>
            <p>Ratings:</p>
            <p class="ratings">${data.Ratings[0].Source}</p>
            <p class="ratings">${data.Ratings[0].Value}</p>
            <p class="ratings">${data.Ratings[1].Source}</p>
            <p class="ratings">${data.Ratings[1].Value}</p>
            <p class="ratings">${data.Ratings[2].Source}</p>
            <p class="ratings">${data.Ratings[2].Value}</p>
            <br>
            <p>Metascore:</p>
            <p class="metascore">${data.Metascore}</p>
            <br>
            <p>imdbRating:</p>
            <p class="imdbRating">${data.imdbRating}</p>
            <br>
            <p>imdbVotes:</p>
            <p class="imdbVotes">${data.imdbVotes}</p>
            <br>
            <p>imdbID:</p>
            <p class="imdbID">${data.imdbID}</p>
            <br>
            <p>Tipologia:</p>
            <p class="tipologia">${data.Type}</p>
            <br>
            <p>Box Office:</p>
            <p class="boxOffice">${data.BoxOffice}</p>
        </div>
    `;

    main.innerHTML += schedaFilm;
}