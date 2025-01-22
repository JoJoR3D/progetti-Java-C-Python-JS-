# Compito 1 (in live)
# Generare un semplice (lmao) programma-quiz che, dati due autori 
# estratti a caso dal file data/authors.json li proponga all'utente 
# domandandogli quale dei due ha pubblicato più album. 
# Qualcosa del tipo:
# Chi ha pubblicato più album fra 'Bello Figo' (1) e 'Queen' (2)?
# L'utente dovrà rispondere con 1 o 2 e il sistema gli dirà se ha vinto 
# o no. 
# Gestire tramite eccezioni l'inserimento di un valore non corretto 
# (né 1, né 2).

# Utilizzare le API di Deezer per capire qual è la risposta corretta e 
# restituire un feedback all'utente. L'API in questione richiede l'id 
# dell'artista, che vi è astutamente fornito nel file data/authors.json.

# Insieme a questo feedback, chiedere anche all'utente se vuole 
# continuare (inserendo il carattere Y) oppure terminare il programma 
# (qualunque altro carattere).



# MI PROCURO I DATI (ARTISTI E NUMERO ALBUM) PER ESEGUIRE IL COMPITO:

import requests
import random

#Accesso al file che contiene gli artisti tramite richiesta API
artist= requests.get("https://raw.githubusercontent.com/Enkkfull/hard-python/main/lezione06/data/artists.json").json()

num_artist= len(artist.keys())
char= "Y"

while char == "Y":
    i= 0
    artista_con_piu_album= ""
    max_album= 0
    artisti_estratti= []
    diz_artisti= {}
    photo_artist= []


    #tramite questo ciclo while ottengo un dizionario contente due artisti (key) e il loro numero di album (values)
    while i < 2:
        #genero un valore casuale che va da 0 al numero di artisti-1 contenuti in artist
        #eseguo un check per controllare che, al secondo ciclo, non venga estratto
        #lo stesso artista estratto al primo ciclo.
        check= 0
        if i == 0:
            artista= random.randint(0,num_artist-1)
            artisti_estratti.append(artista)
        elif i > 0:
            while check == 0:
                artista= random.randint(0,num_artist-1)
                for X in artisti_estratti:
                    if X == artista:
                        break
                    else:
                        check= 1
                
                if check == 1:
                    artisti_estratti.append(artista)
    
        #print(artista)
        

        cont= 0

        #ottengo il nome dell'artista associato al valore casuale generato
        for key in artist.keys():
            #print(f"{key}")
            if cont == artista:
                name_artist= key
        
            cont += 1
    
        print("Artista estratto:", name_artist)

    

   
        stringa_API_for_id= "https://api.deezer.com/search/artist?q=" + name_artist
        #print("Stringa_Api_for_id:", stringa_API_for_id)
        
        #Accesso alle api di deezer per ottenere l'id dell'artista estratto 
        serach_id_artist= requests.get(stringa_API_for_id).json()
        id_artist= serach_id_artist["data"][0]["id"]
        print("id dell'artista:", id_artist)
        #print(serach_id_artist["data"][0]["artist"]["name"])
    
    
    

        stringa_API_for_nb_album= "https://api.deezer.com/artist/" + str(id_artist)
        
        #Accesso alle api di deezer per ottenere il numero di album prodotti 
        #dall'artista fornendo il suo id che ho ricavato dalla chiamata 
        #API di sopra.
        response= requests.get(stringa_API_for_nb_album).json()
        #print(response)
    
        for k,v in response.items():
            #print(f"{key}: {value}")
            if k == "name":
                nome= v 
                print("Nome:", nome)
            if k == "picture_xl":
                photo_artist.append(v)
            if k == "nb_album":
                album= v
                print("Numero di album prodotti:", album)
                if album > max_album:
                    max_album= album
                    artista_con_piu_album= nome

        #creo un dizionario che ha come key: il nome dell'artista; e come value: il numero dei suoi album prodotti
        diz_artisti[name_artist]= album
 
        i= i+1
        print("\n")


    print("\nDIZIONARIO ARTISI:", diz_artisti)
    print("\nArtista con più album:", artista_con_piu_album)

    #salvo in questa lista i nomi dei due artisti estratti
    lista_artisti= []
    for key in diz_artisti.keys():
        lista_artisti.append(key)




    # ESEGUO LA RICHIESTA DEL COMPITO CON I DATI OTTENUTI (ARTISTA E ALBUM PRODOTTI)
    risposta= input(f"\nChi tra {lista_artisti[0]} (vedi foto: {photo_artist[0]})\ne {lista_artisti[1]} (vedi foto: {photo_artist[1]})\nha prodotto più album?\nRispondere 1 per {lista_artisti[0]} 2 per {lista_artisti[1]}\n")

    risp= int(risposta)

    #Sollevo un ECCEZIONE per gestire l'inserimento di un valore non corretto (né 1, né 2)
    try:
        if risp != 1 and risp != 2:
            raise Exception("ERRORE! Le risposte consentite sono 1 per {lista_artisti[0]} e 2 per {lista_artisti[1]}")
        else:
            if artista_con_piu_album == lista_artisti[0] and risp == 1:
                print("\nRISPOSTA GIUSTA!")
            elif artista_con_piu_album == lista_artisti[1] and risp == 2:
                print("\nRISPOSTA GIUSTA!")
            else:
                print("\nRISPOSTA SBAGLIATA!")

    #qui catturo l'eccezione che mi permette di non interrompere il programma, ma lo fa proseguire
    except Exception as error:
        print(error)

    

    #Scegliere se continuare a giocare o terminare il gioco
    char= input("\nSe si vuole continuare a giocaere preme Y altrimenti un qualsiasi tasto\n")
    char= char.upper()
    print("\n")



          



