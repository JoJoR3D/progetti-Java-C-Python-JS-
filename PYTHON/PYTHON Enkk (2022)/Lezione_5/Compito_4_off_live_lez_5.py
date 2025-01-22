# COMPITO 4 (OFF LIVE) Lezione 5

# Creare un semplice sistema che fornisce la temperatura attuale in una 
# provincia italiana richiesta dall'utente.

# Venga dunque richiesta ad un utente tramite input una provincia 
# italiana e tramite le API di Open Meteo ottenere la temperatura e
# temperatura percepita attuale e stamparle. C'è solo un problema: Open Meteo richiede di fornire latitudine e longitudine e non il nome della provincia. Nel file data/province.json potete trovare le latitudini e longitudini di ogni provincia.

# Altri dettagli:

# Se l'input utente non è una provincia, lanciare una eccezione e 
# raccoglierla terminando il programma fornendo un feedback all'utente 
# (qualcosa tipo "Pronvincia non trovata").
# Siete invitati a leggere la documentazione di Open Meteo per capire 
# qual è la chiamata giusta da fare e capire autonomamente come 
# interpretare i dati per trovare la corretta temperatura. 
# Queste API sono un po' ostiche, per gli sviluppatori neofiti 
# suggerisco di leggere la soluzione riportata qui sotto. 
# In ogni caso sarà necessario usare la libreria datetime che non 
# abbiamo mai usato per ottenere l'ora attuale, necessaria per estrarre
# la temperatura corrente.



import requests

from datetime import datetime
# restituisce l'ora attuale come stringa. 
# Esempio: 12 se sono le 12.15, 15 se sono le 15.46, ecc.
hours = datetime.now().strftime("%H") #qui ottengo l'ora

data= datetime.now()    #qui ottengo la data comprensiva di "anno-mese-giorno" con ora,minuti e secondi"
#scompongo la data in modo da ottenere solo: anno-mese-giorno e poi li ricompongo in
#una stringa.
anno= data.year
mese= data.month
giorno= data.day

if giorno <= 9 or mese <= 9:
    if giorno <= 9:
        giorno= '0' + str(giorno)
    elif mese <= 9:
        mese= '0' + str(mese)
    else:
        giorno= '0' + str(giorno)
        mese= '0' + str(mese)


string_day= str(anno) + '-' + str(mese) + '-' + str(giorno) + 'T'

start_time= string_day+hours   #start time
hours= int(hours) + 1
end_time= string_day+str(hours)  #end time



#chiedo la provincia
provincia= input("Inserire la provincia per la quale si vuole ottenere la previsione meteo\n")



#eseguo una richiesta per ottenere il file contene le provincie con le relative latitudini e longitudini
r= requests.get("https://raw.githubusercontent.com/Enkkfull/hard-python/main/lezione05/data/province.json")

#print(r.content)



#eseguo una ricerca nel file delle province per cercare la provincia inserirta
#in input e ottenere la lotitudine e longitudine di questa provincia
for key,values in r.json().items():
    if key == provincia.capitalize():
        latitudine= values["lat"]
        longitudine= values["lon"]



#EXCEPTION
#Se l'utente sbaglia o inserisce una provincia non presente nell'elenco si genera un'eccezione:
#errore: 'NameError' perchè non trovando la provincia non può ottenere latitudine e longitudine (ciclo for sopra)
#che servono da qui in avanti nel programma. Quindi quando l'interprete legge latitudine e longitudine
#ritorna l'errore 'NameError' perchè dice che queste variabili non sono state definite.
#Qui la verifico e poi alla fine la raccolgo

try: 
    print(f"Latitudine: {latitudine}, Longitutine: {longitudine}\n")


    #eseguo una richiesta all'api OpenMeteo a cui passo la latitudine, la longitudine e l'ora di inizio e fine per la ricerca delle previsioni
    response= requests.get(f"https://api.open-meteo.com/v1/forecast?&hourly=temperature_2m,apparent_temperature&timezone=Europe/Rome&latitude={latitudine}&longitude={longitudine}&start_hour={start_time}&end_hour={end_time}")


    #ottengo un file json contenente la temeperatura e la temperatura percepita
    #della provincia inserita nell'arco di ora richiesta
    print(response.json())

    #cerco nel file json la temeperatura e la temperatura percepita e le stampo
    for key,value in response.json().items():
        if key == "hourly":
            temperatura= value["temperature_2m"][0]
            temperatura_percepita= value["apparent_temperature"][0]

    print(f"\nLa temperatura per la provincia di {provincia} è: {temperatura}")
    print(f"La temperatura percepita per la provincia di {provincia} è: {temperatura_percepita}")


except NameError as error:
    print("Provincia non trovata\n")