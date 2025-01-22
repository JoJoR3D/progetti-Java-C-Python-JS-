# COMPITO 2
# Creare un programma che chieda un numero maggiore di 10 ad un utente 
# tramite input e gestisca sia l'eccezione derivante dall'inserimento di 
# un dato che non sia un numero, sia lanci (e gestisca) una eccezione se
# il numero fornito non è maggiore di 10.

num= input("Inserire un valore > di 10\n")

try:
    number= int(num)

#qui solleviamo l'eccezione se number è < 10
    if number < 10:
        raise Exception("Il numero inserito è < di 10")

#qui catturiamo l'eccezione ValueError che si verifica, in questo compito
#quando il codice si aspetta un 'int' ma noi gli diamo in input un 'str'.
except ValueError as Error:
    print(Error)

#qui catturiamo l'eccezione se number è < di 10
except Exception as ex:
    print(ex)











exit(0)










# COMPITO 1.4
# Trova l'utente più ricco

import json

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_5/data.json", "r") as f:
    file= json.load(f)


rich= ""
max_rich= 0
cont= 0

for x in file:
    u= x["name"]
    for y in x["balance"]:
        if y != ',' and y != '$':
            rich= rich + y
    
    print(f"User: {u}, bilance: ${rich}")
    if cont == 0:
        min_rich= float(rich)
        cont += 1

    if float(rich) > max_rich:
        max_rich= float(rich)
        user1= x["name"]

    if float(rich) < min_rich:
        min_rich= float(rich)
        user2= x["name"]
    
    rich= ""

print(f"\n{user1} è l'utente più ricco con un bilancio di: ${max_rich}")
print(f"{user2} è l'utente meno ricco con un bilancio di: ${min_rich}")


















# COMPITO 1.3
# Trova tutti gli utenti attivi

import json

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_5/data.json", "r") as f:
    file= json.load(f)


list_user_active= []

for x in file:
    if x["isActive"]:
        list_user_active.append(x["name"])

print(list_user_active)





















# COMPITO 1.2
# Trovare chi è l'utente che si è registrato prima e per ultimo

import json

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_5/data.json", "r") as f:
    file= json.load(f)



#creo una lista di dizionari contenente il nome dell'utente e
#la data della sua registrazione
list= []

for x in file:
    dict= {}
    if "name" in x:
        dict["name"]= x["name"]
    if "registered" in x:
        dict["registered"]= ""
        for y in x["registered"]:
            if y != "T":
                dict["registered"]= dict["registered"] + y
            else:
                dict["registered"]= dict["registered"] + y
                break
        
    list.append(dict)


#stampo la lista
for x in list:
    print(x)        




print("\n")

#scompongo le date in anni,mesi e giorni e le inserisco in una lista di dizionari insieme all'id dell'utente
date= []
anno= ""
mese= ""
giorno= ""
in_anno=0
in_mese=1
in_giorno=1

for x in list:
    d= x["registered"]
    dict= {}
    dict["name"]= x["name"]
    for y in d:
        if y != '-' and in_anno == 0:
            anno= anno + y
        elif y == '-' and in_anno == 0:
            dict["anno"]= int(anno)
            #print(anno)
            anno= ""
            in_anno= 1
            in_mese= 0

        elif y != '-' and in_mese == 0:
            mese= mese + y
        elif y == '-' and in_mese == 0:
            dict["mese"]= int(mese)
            #print(mese)
            mese= ""
            in_mese= 1
            in_giorno= 0

        elif y != 'T' and in_giorno == 0:
            giorno= giorno + y
        elif y == 'T' and in_giorno == 0:
            dict["giorno"]= int(giorno)
            #print(giorno)
            date.append(dict)
            dict= {}
            giorno= ""
            in_giorno= 1
            in_anno= 0



for x in date:
    print(x)


print("\n")

# trovo l'utente che si è iscritto per prima
anno= 2999
mese= 13
giorno= 32

for x in date: 
    a= x["anno"]
    if a < anno:
        anno = a
        id= x["name"]
    elif a == anno:
        for y in date:
            m= y["mese"]
            if m < mese:
                mese= m
                id= y["name"]
            elif m == mese:
                for j in date:
                    g= j["giorno"]
                    if g < giorno:
                        giorno= g
                        id= j["name"]


#print(anno,mese,giorno)
print("L'utente che si è registrato per prima è:", id)



print("\n")

# trovo l'utente che si è iscritto per ultimo
anno= 0
mese= 0
giorno= 0

for x in date: 
    a= x["anno"]
    if a > anno:
        anno = a
        id= x["name"]
    elif a == anno:
        for y in date:
            m= y["mese"]
            if m > mese:
                mese= m
                id= y["name"]
            elif m == mese:
                for j in date:
                    g= j["giorno"]
                    if g > giorno:
                        giorno= g
                        id= j["name"]


#print(anno,mese,giorno)
print("L'utente che si è registrato per ultimo è:", id)

        














# COMPITO 1.1
# Trovare chi è l'utente che ha il nome dell'amico più lungo

import json

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_5/data.json", "r") as f:
    file= json.load(f)

max= 0

for x in file:
    for y in x["friends"]:
        var= len(y["name"])
        
        if var > max:
            max= var
            id= x["_id"]
            name_friend= y["name"]

print(f"L'id {id} è colui che ha il nome dell'amico: {name_friend} più lungo: {max}")
















# COMPITO 1
# Creare un programma che stampi tutte le mail degli utenti nel file 
# data/01_data.json.

import json

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Lezione_5/data.json", "r") as f:
    
    file= json.load(f)
        
for x in file:
    print(x["email"])

'''
Altro modo:
n= len(file)
    
for i in range(n):
    print(file[i]["email"])
'''


#ora voglio stampare i friends che ha questo id: 62d7f1162bdeb422f55fb77c

for x in file:
    if x["_id"] == "62d7f1162bdeb422f55fb77c":
        print(x["friends"])
        

print("\n")

#ora voglio stampare quanti friends ha questo id: 62d7f1162bdeb422f55fb77c

cont= 0

for x in file:
    if x["_id"] == "62d7f1162bdeb422f55fb77c":
        for y in x["friends"]:
            print(y)
            cont += 1

print(f"L'id 62d7f1162bdeb422f55fb77c ha {cont} friends")















import requests

response= requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())
print(response.json()["title"]) #accedere al titolo 




















import requests
response= requests.get('https://github.com')

#riceveremo come risposte un codice: 200 che sta ad indicare che la richiesta è andata a buon fine
print(response)

#ritorna la pagina html di github
#print(response.content)

#header della richiesra http
print(response.headers)