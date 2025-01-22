# JSON (non è un tipo di file ma una codifica del file (è un modo di scrivere testo))
# json viene rappresentato come una lista

# questo formato si chiama JSON (https://www.json.org/json-en.html)
# nel quale dizionari, liste, interi e stringhe sono facilmente codificati come testo
# in python è prima di tutto necessario importare il modulo json

import json

# È possibile lavorare con json sia a partire da stringhe che da file. Se lavoriamo con stringhe possiamo:

my_json_string = '{"name": "Bob", "languages": ["Python", "Java"]}'
now_its_an_object = json.loads(my_json_string) # converte una stringa in formato json in un oggetto python classico

# oppure, all'inverso

person_dict = {'name': 'Bob', 'age': 12, 'children': None }
person_json = json.dumps(person_dict) #converte un oggetto di python in un json equivalente

 
# https://www.programiz.com/python-programming/json

# La stessa cosa è possibile utilizzando direttamente dei file json.
# notare che .loads() e .dumps() si usano per le stringhe
# mentre .load() e .dump() si usano per i file.

# lettura:
with open('path_to_file/person.json', 'r') as f:
  data = json.load(f)

# scrittura
with open('path_to_file/person.json', 'w') as f:
	json.dump(data, f, indent=3)
     





#REQUESTS

# Un programma ha spesso necessità di collegarsi a siti esterni per ottenere informazioni
# che poi processerà per ottenere un risultato.

# Vi sono diversi modi per farlo, ma uno dei più comuni dei recenti anni sono le cosiddette
# API REST. Le API rest ci permettono di ottenere programmaticamente dati da siti web in maniera sicura e veloce

# Siti che ci tornano non solo l'header in json ma anche il body sono pagine che offrono delle API REST.
# Ad esempio teitch o youtube metto a disposizione dei dati (API REST) in json.

# La comunicazione con API REST avviene attraverso il protocollo HTTP (di cui non parleremo qui)
# ma ci limitiamo a dire che si tratta una comunicazione stateless di "pacchetti di dati" le cui parti fondamentali sono head e body. Nell'head si forniscono informazioni relative al tipo di pacchetto e autorizzazioni, mentre nel body ci sono i dati effettivi. Le comunicazioni HTTP non sono tutti uguali, ma ci sono diversi metodi: GET, POST, PUT e altri. Tralasciamo comunque queste complicatezze e limitiamoci a pastrocchiare con qualche API. 

# Poiché come detto l'accesso alle API avviene col protocollo HTTP, dobbiamo effettuare una *richiesta http* in python e ciò è possibile usando le funzionalità del pacchetto requests

import requests

# https://pypi.org/project/requests/

# Le requests sono generiche richieste HTTP (le stesse che facciamo col browser), quindi ci permettono di fare di più che solo usare API web. 

# ad esempio:

response = requests.get('https://github.com')

# ci fornirà nella variabile response il sito web di github

# se però stampiamo direttamente la response otterremo soltanto un codice (200), che ci indica che la richiesta è andata a buon fine

print(response)

# possiamo accedere all'effettivo contenuto della risposta così:

print(response.content)

# gli header invece sono accessibili tramite:

print(response.headers)

##########################################################################################

# Vediamo ora come usare le request per ottenere dati da un ipotetico servizio

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.content)

# possiamo notare che la risposta a questa request è in JSON! Infatti le API REST comunicano sempre in 
# JSON, motivo per il quale è un formato così importante. Infatti, possiamo fare:

response_but_json = response.json()
print(response_but_json)

# per avere i dati forniti dal sito web in json direttamente trattabile in python
# come si vede, stiamo usando il metodo *get* delle request, quindi è una richiesta di ottenere qualcosa.
# possiamo anche - volendo - fornire noi stessi dati al gestore delle API (ad esempio potremmo voler postare un tweet su twitter via APIs). In tal caso dobbiamo ricorrere al metodo POST .post() o .put() a seconda della definizione delle API in questione

# infine, un altro tema importante: la sicurezza. Naturalmente se vogliamo postare un Tweet su Twitter o se vogliamo avere il numero di subscribers da Twitch via API, dobbiamo autenticarci. Queste informazioni non sono di dominio pubblico. L'autenticazione si può svolgere in diversi modi (alcuni anche piuttosto complessi). Uno dei modi più semplici consiste nell'avere una API KEY che deve essere inserita nell'header di ogni chiamata.

#Ecco un esempio

# definire token e url
token = "LMAO-IL-TOKENONE"
url = "URL_PER_LA_RICHIESTA"

# l'header è un dizionario!
headers = {'Authorization': "Bearer {}".format(token)}

# finalmente fare la richiesta
response = requests.get(url, headers=headers)

# il tema è complesso e ci sono moltissimi use case. Lascio qui una guida completa per chi è interessato ad approfondire: https://realpython.com/api-integration-in-python/











# EXCEPTION

# Un programma python termina quando incontra un errore. In python vi sono due grandi famiglie di errori: syntax errors e exceptions. I primi sono errori di sintassi derivanti da un codice scritto male:

# print("ciao")) 

# c'è una parentesi di troppo, dunque otterremo un "SyntaxError: invalid syntax"

# se invece proviamo a fare 

# print(0/0) 

# non avremo errori di sintassi bensì una exception


# Python offre la possibilità di gestire le exception ed in particolare di "sollevare" le nostre exceptions e anche di catturare quelle che possono accadere durante l'esecuzione. Iniziamo a vedere come possiamo lanciare delle custom exceptions


############## GENERARE EXCEPTIONS #######################

# Diciamo di aspettarci in input un valore maggiore di cinque:

x = int(input("Inserisci un valore maggiore di 5"))
if x <= 5:
    raise Exception("Ti avevo detto maggiore di cinque, capra")

# grazie alla dicitura "raise Exception()" possiamo lanciare una nostra eccezione generica con un testo configurabile e così facendo interrompere l'esecuzione del codice


# possiamo anche fare delle asserzioni che -se riscontrate false- interromperanno l'esecuzione del programma. Ecco come farlo:

import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

# in questo caso stiamo asserendo che il sistema sul quale deve girare il programma deve essere Linux. Se lo è, procederemo senza problemi, altrimenti incapperemo in una AssertionError exception

############## CATTURARE EXCEPTIONS #######################

# oltre che generare le nostre exception, abbiamo anche bisogno di catturare quelle del sistema. 
# un esempio tipico è la lettura di file che potrebbero non essere presenti sul sistema. Vediamolo.

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

# se il file 'file.log' non dovesse esistere, la funzione open lancia una FileNotFoundError exception che
# qui intercettiamo. Il blocco di codice che può produrre l'exception deve essere incluso nella 'try', mentre l'except contiene il codice che viene eseguito SE l'eccezione viene lanciata. 

# È buon costume restringere l'except al tipo esatto di eccezione che vogliamo catturare. Nel nostro caso:

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# specificando il tipo FileNotFoundError dopo l'except e indicando che vogliamo salvarla nella variable fnf_error, possiamo direttamente stamparla e la nostra except verrà eseguita SOLO se l'exception sollevata nella try è di tipo FileNotFound. È possibile accodare più except, a seconda del tipo di exception sollevata

"""
try: 
	una_funzione_che_potrebbe_lanciare_due_tipi_di_exceptions()
except Tipo1 as error:
	print(error)
  fare_qualcosa()
except Tipo2 as error:
	print(error)
  fare_qualcosaltro()
"""

# qui a seconda del tipo di eccezione eseguiamo il metodo fare_qualcosa() o fare_qualcosaltro()


# è possibile anche specificare un blocco di codice che venga eseguito se nessuna exception è lanciata (tramite l'else) e un blocco di codice che venga eseguito indipendentemente dalle exception (magari una funzione di pulizia finale) tramite il finally. Lascio qui come sempre un riferimento completo: https://realpython.com/python-exceptions/