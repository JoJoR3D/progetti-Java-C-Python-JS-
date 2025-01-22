#SET
#E' un insieme di elementi non ordinati (non ci sono indici), unici (non ci possono essere duplicati) e
#immutabili.
#si dichiarano con le parentesi graffe
#.add() per aggiungere un elemento al set, .remove() per rimuoverlo

#Un esempio pratico di utilizzo dei set è ad esempio ho una lista con degli elementi
#duplicati, allora li passo ad un set che in automatico mi elimina gli elementi duplicati
#Esempio:
print("Rimuovere gli elementi da una lista passandoli ad un set")

l1= ["mamma", "sorella", "nonna", "nonno", "sorella", "zio"]
my_set= set()
print(l1)

for x in l1:
    #print(x)
    my_set.add(x)

print(my_set)


#NOTA BENE:
'''
x = [1, 2, 3] # is a literal that creates a list (mutable array).  
x = []  # creates an empty list.

x = (1, 2, 3) # is a literal that creates a tuple (constant list).  
x = ()  # creates an empty tuple.

x = {1, 2, 3} # is a literal that creates a set.  
x = {}  # confusingly creates an empty dictionary (hash array), NOT a set, because dictionaries were there first in python.  

USO QUESTA DECITURA PER CREARE UN SET VUOTO:
x = set() # to create an empty set.

'''





#TUPLE
#sono un insieme di elementi ordinati, immutabili e possono contenere duplicati.

print("\nTUPLE:")

my_tuple= {"maschio", "femmina", "altro"}

gender= input("Gender: ")

if gender.lower() not in my_tuple:
    print("\nValore non accettato")







#STRING MANIPULATION
print("\nSTRING MANIPULATION")
#per usare le virgolette in una stringa possiamo usare il carattere di escape, ovvero backslash.

txt= "Ciao \"Enkk\", come stai?"

print(txt)

#altro modo è usare il singolo apice per identificare la stringa e il doppio apice per mettere
#la parola tra virgolette

txt= 'Ciao "Enkk" come stai?'

print(txt)

#il backslash può essere usato anche per dei caratteri speciali, ad esmepio per andare
#a capo si usa '\n'

#'\t' per il tab





#Possiamo usare l'operatore 'in' per trovare il carattere o una sottostringa all'interno di una stringa

print("\nEsercizio 1:")

txt= 'Ciao "Enkk" come stai?'

print('z' in txt)





#in un certo senso le stringhe sono delle liste di caratteri 

print("\nEsercizio 2:")

txt= 'Ciao "Enkk" come stai?'

print(txt[2])






#possiamo usare, con le stringhe, la funzione .find() che ci restiuisce la posizione della prima occorenza di 
#quel carattere all'interno della stringa

print("\nEsercizio 3:")

txt= 'Ciao "Enkk" come stai?'

print(txt.find('k'))








#Funzioni da usare per le STRINGHE

'''
.upper()      tutto in maiscolo
.lower()      tutto in minuscolo
.capitalize() la prima lettera della stringa in maiuscolo
.title()      la lettera iniziale di ogni parola dopo uno spazio in maiscolo

'''

txt= 'Ciao "Enkk", come stai?'

print("\nFUNZIONI:")

print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.title())




#.strip()
#ci permette di togliere dall'inizio e dalla fine della stringa dei caratteri
#se allo strip non passiamo nulla ( .strip() ), vuol dire che eliminerà gli spazi alla fine e inizio di una stringa

txt= '..+..Ciao "Enkk", come stai?....'

print("\n.strip()")
print(txt)
print(txt.strip('.+')) #toglierà i puntini e il '+' che stanno all'inizio e/o alla fine della stringa




#.replace()
#permette di rimpiazzare un carattere (anche se si ripete più di una volta) all'interno della stringa

txt= 'Ciao "Enkk", come stai?'

print("\n.replace()")

print(txt.replace('a', 'A')) #rimpiazzo il carattere 'a' minuscolo con quello maiuscolo 'A'





#.split()
#scompone una stringa inserendola in una lista. Per farlo gli dobbiamo passare il carattere che verrà usato come divisore della stringa.
#Esempio:

txt= "Silicon Valley"

#passandogli il carattere 'i', la stringa sarà così scomposta nella lista:

#[s,l,con Valley]

print("\n.split()")

print(txt.split('i')) 





#.join()
#unisce gli elementi di una lista in una stringa.
#prima di chiamare la funzione dobbiamo indicare il carattere che verrà usato per dividere 
#gli elementi della lista nella stringa. Ad esempio lo spazio " ". 
#alla funzione .join(lista) passiamo invece la lista.

list= ["Ciao", "mamma,", "come", "stai?"]

print("\n.join()")

stringa= " ".join(list)

print(stringa)






#Funzioni di formattazione della stringa in output
#.format()
#ci permette di sostituire le parentesi graffe all'interno di una stringa con
#delle stringhe
#Esempio:

txt= "Ciao sono {name} e sono molto bello!"

print("\n.format()")

print(txt.format(name= "Enkk"))


#le parentesi graffe possono essere anche vuote.

txt= "Ciao sono {} e sono molto bello!"

print(txt.format("Enkk"))


#si specifica un nome all'interno delle parentesi graffe quando inseriamo più
#parentesi graffe all'interno di una stringa.

txt= "Ciao sono {name} e sono molto bello! Anche molto {aggettivo}"

print(txt.format(name= "Enkk", aggettivo= "intelligente"))

print(txt.format(name=input("Inserisci nome: "), aggettivo=input("Inserisci aggettivo: ")))









# SLICING! 

# una cosa importante che si può fare in python su ogni elemento indicizzato (quindi le stringhe, ma anche le liste in generale) è lo slicing. 

# anziché fornire un indice (che tral'altro vanno anche al contrario, quindi -1 è l'ultimo elemento) si fornisce un intervallo
# di indici nella forma [start:step:stop]
# questo crea delle fettine (da cui, slicing).
# per semplicità ignoriamo il valore step (che di default è 1), e consideriamo start come il primo indice che farà parte della fetta
# e come stop il primo ESCLUSO dalla fetta. quindi l'indice di stop NON è inserito nella slice.
# ergo, [1:5] prenderà gli elementi in indice 1, 2, 3 e 4.
# se start non viene specificato si parte dal primo indice disponibile, se stop non viene definito si considera l'ultimo indice +1 (così da darci l'ultimo elemento)
# quindi [:3] fornisce una slice contenente i primi tre elementi, [3:] fornisce una slice che va dal terzo elemento fino al fondo

my_str = 'yellow'

print("\nSLICING:\n", my_str)

print(my_str[1])     # => 'e'
print(my_str[-1])   # => 'w'
print(my_str[4:6])   # => 'ow'
print(my_str[:4])    # => 'yell'
print(my_str[-3:])   # => 'low'

# come detto funziona anche sulle liste
my_list = ["ciao", "amici", "miei", "come", "state"]

print(my_list[:2]) # ["ciao", "amici"]





#voglio inserire in un dizionario una classifica di tutti i giochi dei tre utenti

u1= {"utente": "paolo", "games": ["carte", "briscola", "roulette"]}
u2= {"utente": "luca", "games": ["dadi", "roulette", "sala slot"]}
u3= {"utente": "lucia", "games": ["briscola", "carte", "dadi"]}

user= [u1,u2,u3]

#qui stampo l'elemento all'indice 2 della lista games presente 
#nel dizionario u2 che a sua volta si trova nella lista user
#questo è solo per vedere come chiamare un valore di una lista (games) contenuta
#in un dizionario (u2) che a sua volta è contenuto nel dizionario (user)
print(user[1]["games"][2])

diz_game= {}

for id in user:
    for game in id["games"]:
        cont= 0
        if game in diz_game:
            diz_game[game]= diz_game[game] + 1
        else:
            cont += 1
            diz_game[game]= cont

print(f"Lista giochi: {diz_game}\n")




#aggiungo i giochi preferiti di tutti gli utenti in un'unica lista
games= []

for id in user:
    for game in id["games"]:
        games.append(game)
        

#qui trovo qual è il gioco o quali sono i giochi più preferiti da tutti gli utenti
n= len(games)
cont=0
cont_max= 0
giochi_preferiti= set()

for i in range(n):
    for y in games:
        if y == games[i]:
            cont += 1

    if cont >= cont_max:
        cont_max= cont
        index= i
        giochi_preferiti.add(games[index])
    
    cont= 0

print(f"\nGioco o giochi preferiti da tutti gli utenti: {giochi_preferiti}, cont: {cont_max}\n")





#altro modo per trovare il gioco o i giochi preferiti da tutti gli utenti
#usando la coppia chiave/valore del dizionario diz_game{} creato sopra (riga 292)

max= 0
game_favorite= []

for gameplus in diz_game:
    #print(gameplus)    gameplus ritorna il valore di ogni chiave del dizionario: diz_game{}
    if diz_game[gameplus] >= max:
        max= diz_game[gameplus]
        game_favorite.append(gameplus)

print(f"Gioco o giochi preferiti da tutti gli utenti: {game_favorite}")




#altro modo per trovare il gioco o i giochi preferiti da tutti gli utenti
#usando la coppia chiave/valore del dizionario diz_game{} mediante .items()

max= 0
game_favorite= []

# .items() ritorna la coppia chiave (game) / valore (game_count)
for game, game_count in diz_game.items(): 
    #print(gameplus)    gameplus ritorna il valore di ogni chiave del dizionario: diz_game{}
    if game_count >= max:
        max= game_count
        game_favorite.append(game)

print(f"Gioco o giochi preferiti da tutti gli utenti: {game_favorite}")






#FUNZIONI E METODI

#i METODI sono chiamati su di una variabile
#ad esempio i metodi .keys(), .values(), .items() per i dizionari
#Esempio: dict.keys()