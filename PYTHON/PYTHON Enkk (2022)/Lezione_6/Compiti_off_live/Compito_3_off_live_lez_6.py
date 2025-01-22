# Compito 03 (off live)
# Modificare il Compito 1 in modo da chiedere di indovinare chi ha più 
# fan e non chi ha più album. Aggiungere anche nuovi artisti e testare che
# le chiamate API funzionino.

# Per trovare l'd ID di altri artisti è necessario utilizzare l'API 
# search di deezer. Dato che vi voglio bene ho già preparato uno script
# che potete modificare qui: get_artists_ids.py. 
# Cambiate la lista degli artisti da cercare e copincollate il 
# risultato della computazione nel file data/artists.json. 
# Potete anche modificare lo script in modo da scrivere direttamente il 
# json dentro artists.json!

import requests
import random
import json


lista_cantanti= []

#Accesso al file preso dal web che contiene i cantanti
with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_6/Compiti_off_live/clean_data.json", "r") as f:
    file= json.load(f)

for key, value in file.items():
    if key == "master_metadata_album_artist_name":
        for chiave,valore in value.items():
            lista_cantanti.append(valore)   #ottengo una lista di tutti i cantanti


#print(len(lista_cantanti))


# MI PROCURO I DATI (ARTISTI E NUMERO ALBUM) PER ESEGUIRE IL COMPITO:

num_artist= len(lista_cantanti)
char= "Y"

while char == "Y":
    i= 0
    artista_con_piu_fan= ""
    max_num_fan= 0
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
        for var in lista_cantanti:
            #print(f"{key}")
            if cont == artista:
                name_artist= var
        
            cont += 1
    
        print("Artista estratto:", name_artist)

    

   
        stringa_API_for_id= "https://api.deezer.com/search/artist?q=" + name_artist
        #print("Stringa_Api_for_id:", stringa_API_for_id)
        
        #Accesso alle api di deezer per ottenere l'id dell'artista estratto 
        serach_id_artist= requests.get(stringa_API_for_id).json()
        id_artist= serach_id_artist["data"][0]["id"]
        print("id dell'artista:", id_artist)
        #print(serach_id_artist["data"][0]["artist"]["name"])
    
    
    

        stringa_API_for_nb_fan= "https://api.deezer.com/artist/" + str(id_artist)
        
        #Accesso alle api di deezer per ottenere il numero di fan 
        #dall'artista fornendo il suo id che ho ricavato dalla chiamata 
        #API di sopra.
        response= requests.get(stringa_API_for_nb_fan).json()
        #print(response)
    
        for k,v in response.items():
            #print(f"{key}: {value}")
            if k == "name":
                nome= v 
                print("Nome:", nome)
            if k == "picture_xl":
                photo_artist.append(v)
            if k == "nb_fan":
                fan= v
                print("Numero di fan:", fan)
                if fan > max_num_fan:
                    max_num_fan= fan
                    artista_con_piu_fan= nome

        #creo un dizionario che ha come key: il nome dell'artista; e come value: il numero dei suoi fan
        diz_artisti[name_artist]= fan
 
        i= i+1
        print("\n")


    print("\nDIZIONARIO ARTISI:", diz_artisti)
    print("\nArtista con più fan:", artista_con_piu_fan)

    #salvo in questa lista i nomi dei due artisti estratti
    lista_artisti= []
    for key in diz_artisti.keys():
        lista_artisti.append(key)




    # ESEGUO LA RICHIESTA DEL COMPITO CON I DATI OTTENUTI (ARTISTA E ALBUM PRODOTTI)
    risposta= input(f"\nChi tra {lista_artisti[0]} (vedi foto: {photo_artist[0]})\ne {lista_artisti[1]} (vedi foto: {photo_artist[1]})\nha un maggior numero di fan?\nRispondere 1 per {lista_artisti[0]} 2 per {lista_artisti[1]}\n")

    risp= int(risposta)

    #Sollevo un ECCEZIONE per gestire l'inserimento di un valore non corretto (né 1, né 2)
    try:
        if risp != 1 and risp != 2:
            raise Exception("ERRORE! Le risposte consentite sono 1 per {lista_artisti[0]} e 2 per {lista_artisti[1]}")
        else:
            if artista_con_piu_fan == lista_artisti[0] and risp == 1:
                print(f"\nRISPOSTA GIUSTA! L'artista con più fan è {artista_con_piu_fan}")
            elif artista_con_piu_fan == lista_artisti[1] and risp == 2:
                print(f"\nRISPOSTA GIUSTA! L'artista con più fan è {artista_con_piu_fan}")
            else:
                print(f"\nRISPOSTA SBAGLIATA! L'artista con più fan è {artista_con_piu_fan}")

    #qui catturo l'eccezione che mi permette di non interrompere il programma, ma lo fa proseguire
    except Exception as error:
        print(error)

    

    #Scegliere se continuare a giocare o terminare il gioco
    char= input("\nSe si vuole continuare a giocaere preme Y altrimenti un qualsiasi tasto\n")
    char= char.upper()
    print("\n")


