# COMPITO 3
# Effettuare una request e analizzare il json 
# in https://jsonplaceholder.typicode.com/todos. 
# Stampare dunque per ogni utente (le cui informazioni sono ottenibili 
# qui https://jsonplaceholder.typicode.com/users) una tabella 
# (usando PrettyTable) per ogni utente, mostrando la lista dei task e 
# una spunta (o X) a seconda che il task sia completato o meno.

# Esempio:

'''
+-----------+------------+
|   Marco   |    TODO    |
+-----------+------------+
| Lavarsi   |     X      |
| Spesa     |     ✓      |
|    ...    |      ...   |
+-----------+------------+
'''

import requests
from prettytable import PrettyTable
table = PrettyTable()

response= requests.get("https://jsonplaceholder.typicode.com/todos") #lista dei todo
response2= requests.get("https://jsonplaceholder.typicode.com/users") #lista degli utenti

#print(response.json())

#mi permete di vedere il primo user della lista todo
#print(response.json()[0])

#facciamo un dizionario che ha come key: userId, mentre
#ha come values: liste di todo ("id", "title", "completed") di quel utente.
dict= {}

for x in response.json():
    if x["userId"] in dict.keys():  #Se l'utente ("userId") è già presente nel dizionario gli vado ad aggiungere il todo (x)
        dict[x["userId"]].append(x)
    else:
        dict[x["userId"]]= [x]  #Se invece l'utente ("userId") non è presente nel dizionario, vado a creare la key: dict[x["userId"]] e assegno a questa chiave, come valore, una nuova lista in cui aggiungo il todo ([x])

    #print(x["title"],x["completed"])

#print(dict)





#prendo da response2 tutti i name degli utenti e li salvo in una lista
name= []

for x in response2.json():
    name.append(x["name"])

#print(name)





# Stampo per ogni utente una tabella contenente su ogni riga i
# "title" (ovvero i todo da fare) e i "completed" che indica se 
# quel todo è stato fatto oppure no.

for key in dict:        #scorro un "userId" (key) alla volta. Nota che in questo caso la Key è un valore INTERO
    n= len(dict[key])   #ogni "userId" contiene dieci "id", quindi n per ogni "userId" sarà == a 10  
    for i in range(n):  #per ogni "userId" scorro la sua lista e stampo nella tabella i valori delle key: "title" e "completed"
        #print(dict[key][i])
        table.field_names= [name[key-1], "TODO"] #il campo nome di ogni tabella avrà come titolo: il nome dell'utente e la stringa "TODO".
        
        if dict[key][i]["completed"]:
            simbolo= '✔'   #se il todo è stato completato, quindi è True, metto la spunta
        else:
            simbolo= 'O'    #se il todo NON è stato completato, quindi è False, metto il cerchio

        table.add_row([dict[key][i]["title"],simbolo])
    
    print(table)    #dopo aver creato le righe per tutte le key "title" e "completed" del "userId", stampo la tabella
    table = PrettyTable() #poi aggiorno la tabella in modo da pulirla per crearne una nuova per il prossimo "userId"



