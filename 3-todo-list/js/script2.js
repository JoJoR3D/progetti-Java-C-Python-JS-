
const form = document.querySelector(".input-ricerca");

/*
Spiegazione della regex:
^: Questo carattere indica l'inizio della stringa. Significa che la corrispondenza deve iniziare dall'inizio della stringa.
(?!\s*$): Questa parte è un "negative lookahead assertion" (asserzione di anticipazione negativa). In pratica, 
          verifica che non ci sia una sequenza di spazi vuoti (rappresentati da \s) fino alla fine della stringa ($). 
          In altre parole, esclude le stringhe vuote o composte solo da spazi.
.+: Questo indica uno o più caratteri qualsiasi (.) almeno una volta (+).

L'asterisco (*) dopo la s nella parte \s* indica che possono esserci zero o più occorrenze di spazi bianchi.
*/
const regex = /^(?!\s*$).+/;


/*Ascoltiamo l'evento 'keyup'*/
form.addEventListener('keyup', e => {
    
    /*blocchiamo il refresh della pagina che abbiamo con il form*/
    e.preventDefault();
    
    /*Aggiungi task*/
    /*Aggiungiamo i task che inseriamo nel campo input con name="add" solo se premiamo il tasto invio ('Enter') e se non vengono inseriti una
    sequenza o un singolo spazio vuoto senza nessun carattere.
    N.B. Se aggiungiamo una serie di spazi e poi un carattere (o un astringa) prenderà solo il carattere senza gli spazi iniziali
         grazie alla regex*/
    if (e.key=='Enter' && regex.test(form.add.value)) {
        
        /*il toDo conterrà il task inserito dall'utente*/
        let toDo = form.add.value;
        /*Dopo aver inseito il task e averlo salvato nella variabile toDo, svuotiamo il campo del input con name="add"*/
        form.add.value = '';
        
        /*creiamo il tag vuoto li*/
        let li = document.createElement("li");

        /*slezioniamo la lista con tag ul e classe 'ulista' per poi aggiungerci il tag li*/
        let lista = document.querySelector('.ulista')
        
        console.log(toDo);
        
        /*inserisco nel tag li il primo div che conterrà il task e il secondo div che contiene l'immagine del cestino*/
        li.innerHTML = `<div></div><div><img src="./images/bin.png" alt="cestino" class="bin"></div>`;
        
        /*aggiungo al tag li la classe CSS 'elemento-lista' che definisce lo stile della nostra lista di task*/
        li.classList.add('elemento-lista') 
        
        /*aggiungiamo il tag li alla pagina html*/
        /*
            appendChild: Questo è un metodo degli elementi HTML. 
            La sua funzione è quella di aggiungere un elemento come 
            ultimo figlio di un altro elemento. In altre parole, "appende" 
            un nuovo elemento alla fine di una lista di elementi figli.
        */
        lista.appendChild(li);

        //console.log(li.children[0]);


        /*Qui facciamo si che dopo che l'utente ha premuto invio per aggiungere il task scritto alla lista,
        il task venga aggiunto un carattere alla volta dopo un certo tot di millisecondi. Per fare questo 
        abbiamo usato un metodo della classe window: setInterval() che accetta come primo parametro un'arrow
        function e come secondo il tempo espresso in millisecondi dopo il quale far succedere quello indicato
        dalla arrow function*/

        /*Prendo il primo figlio del tag li, ovvero il primo div che conterrà il task*/
        let figlioLi= li.children[0];

        let output= "";
        let contenitore= "";
        let i= 0;
        let temp= setInterval(() => {

            if(output == toDo)      /*quando la stringa output sarà uguale alla stringa toDo allora interrompo il setInterval con clearInterval(temp)*/
                clearInterval(temp);
            else{
                contenitore= toDo[i];   /*gli assegno di volta in volta un carattere del toDo (che contiene la stringa task)*/
                figlioLi.textContent += contenitore; /*aggiungo il carattere nel div della pagina html*/
                output += toDo[i];  /*gli assegno di volta in volta i caratteri della stringa task*/
            }
            i++; /*incremento l'indice per prendere il carattere della stringa toDo*/

        }, 100); /*tempo espresso in millisecondi*/
        
    }


    /*Cerca Task*/ 
    /*Ad ogni 'keyup' vedo se il carattere inserito è presente (includes) in uno dei task*/
    /*Lo stesso ai prossimi caratteri inseriti, vedo se sono inclusi in uno o più task. Se
    si mi verrano mostrati solo i task corrispondenti.*/

    /*ricerca conterrà il task che l'utente vuole cercare nella lista e che inserisce nal campo
    con tag input che ha name="cerca*/
    let ricerca = form.cerca.value;
    
    console.log(ricerca);

    /*seleziono tutti i tag 'li' e li inserisco in un array*/
    /*L'array conterrà ad esempio questo: <li class="elemento-lista"></li>*/
    let arrLista = document.querySelectorAll("li");
   
    /*ciclo sul array */
    arrLista.forEach(elemento => {

        console.log(elemento.innerText);
        
        /*elemento.innerText: di elemento mi prendo il contenuto testuale, ovvero il task*/
        /*Sto dicendo che se quello scritto in ricerca (carattere/sequenza di caratteri) NON è incluso in uno dei task,
        allora verrà aggiunto ad ogni task che non ha corrispondenza con la stringa ricerca la classe 'hide'.
        Questa classe applica display none all'elemento <li> che contiene il task*/
        /*Sulla ricerca applico una regex per verificare che quello inserito dall'utente non contenga spazi all'inizio e fine della stringa,
        se li contiene non fa comparire nulla nella lista dei task.*/
        /*In alternativa avremmo potuto usare:

            if (!elemento.innerText.toLowerCase().includes(ricerca.toLowerCase().trim())

        Il metdodo .trim() elimina gli spazi all'inizio e alla fine della stringa di ricerca. In questo modo se quello ricercato è presente 
        nella lista comparirà. 
        */
        if (!elemento.innerText.toLowerCase().includes(ricerca.toLowerCase()) && regex.test(ricerca)) {
            elemento.classList.add('hide');
        }
        /*altrimenti se l'utente sta cancellando (tasto Backspace) quello scritto nel campo ricerca,
        verifica se, a ogni 'keyup', i caratteri rimasti in 'ricerca' sono inclusi in 'elemento.innrerText' (task). 
        Se si, rimuove la classe 'hide' all'elemento <li> che contiene il task 
        (ovviamente se quel tag li ha la classe 'hide' applicata)*/
        else if(e.key=='Backspace'){
            elemento.classList.remove('hide');
        }

        /*altrimenti se l'utente preme invio svuoto l'input con nome="cerca" per la ricerca dei task*/
        else if(e.key === 'Enter'){
            form.cerca.value= "";
        }
    
    }); 
    
    
});


/*Elimina task*/
/*Elimino i task se clicco sul icona del cestino*/

/*seleziono il tag che contiene la classe 'bin'*/
const cestino = document.querySelector('.bin');

/*ascolto l'evento di click nel form*/
form.addEventListener('click', e => {
    e.preventDefault();
    
    console.log(e);
    
    /*Se l'utente clicca sul cestino*/
    if (e.target.className==='bin') {
        
        /*Qui stiamo prendendo il padre del tag <img> che contiene il cestino che abbiamo premuto. 
        Il padre è il div che contiene il tag <img> del cestino*/
        //console.log(e.target.parentElement);
        
        /*Qui prendiamo il padre del div visto sopra. Il padre del div visto sopra 
        è il tag <li> che contiene il div del task (primo figlio) 
        e il div dell'immagine del cestino (secondo figlio).*/
        //console.log(e.target.parentElement.parentElement);
        
        /*Quindi stiamo rimuovendo il tag <li> che vogliamo eliminare avendo premuto sul suo cestino*/
        e.target.parentElement.parentElement.remove();
    }
    
});



