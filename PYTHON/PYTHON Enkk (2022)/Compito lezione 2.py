#COMPITO 1
#Dichiarare due liste di numeri con cinque elementi ciascuna e creare una lista concatenata che le includa entrambe.
#Bonus: prendere gli elementi dalle due liste chiedendoli uno per uno (mediante input)

#COMPITO 2
#Dichiarare una lista e stampare il reverse (senza usare altre variabili)

#COMPITO 3
#Modificare l'esercizio del casinò (lezione 1 compito 1) in un registro degli utenti del suddetto. Creare un interfaccia da terminale per aggiungere n utenti.
#Salvare ciascuno in un dizionario (e dunque in una lista che li contenga tutti). Il programma deve rifiutare un intersezione se il nickname di uno degli utenti è già presente nel dizionario.

'''
Finita l'inserzione, creare un modulo statistico che analizzi i dati inseriti nel sistema.
In particolare si vuole sapere:
la percentuale di maschi e di femmine e la età massima, minima e media dei registrati.

'''

'''
Struttura utente:
Nickname
Eta
Gender

'''


'''
Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esmepio liste.

'''





#ESECUZIONE

#COMPITO 1
#Dichiarare due liste di numeri con cinque elementi ciascuna e creare una lista concatenata che le includa entrambe.
#Bonus: prendere gli elementi dalle due liste chiedendoli uno per uno (mediante input)


list1= []
list2= []
list3= []

#inserisco i 5 valori nelle due liste

for i in range(5):
    numb1= input(f"Inserire {i+1} valore della lista 1: ")
    numb2= input(f"Inserire {i+1} valore della lista 2: ")
    list1.append(int(numb1))
    list2.append(int(numb2))

    if list1[i] < list2[i]:
        list3.append(list1[i])
        list3.append(list2[i])
    else:
        list3.append(list2[i])
        list3.append(list1[i])


print("lista_1:", list1)
print("lista_2:", list2)
print("lista_concatenata:", list3)






#COMPITO 2
#Dichiarare una lista e stampare il reverse (senza usare altre variabili)

l= [0,1,2,3,4,5,6,7,8,9]
n= len(l)

print("\nReverse della lista: ")
for x in range(n-1,-1,-1):
    print(l[x])






#COMPITO 3
#Modificare l'esercizio del casinò (lezione 1 compito 1) in un registro degli utenti del suddetto. Creare un interfaccia da terminale per aggiungere n utenti.
#Salvare ciascuno in un dizionario (e dunque in una lista che li contenga tutti). Il programma deve rifiutare un intersezione se il nickname di uno degli utenti è già presente nel dizionario.
'''
Finita l'inserzione, creare un modulo statistico che analizzi i dati inseriti nel sistema.
In particolare si vuole sapere:
la percentuale di maschi e di femmine e la età massima, minima e media dei registrati.

'''
'''
Struttura utente:
Nickname
Eta
Gender

'''
'''
Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esmepio liste.

'''



lista= []
games= []
g= set()

for i in range(2):
    utente= {}

    nick= input("Nickname: ")

    #verifico che il Nickname inserito non sia già stato utilizzato da un altro utente
    if i > 0:
        n= len(lista)
        y= 0
        flag= 0
        while y < n:
            if nick == lista[y]["Nickname"]:    #la lista conterrà 5 dizionari, a lista[0] vi è il primo dizionario, a lista[1] il secondo, ecc..
                print("Nickname già utilizzato, reinserirne uno nuovo grazie.")
                nick= input("Nickname: ")
                flag= 1
            
            if flag == 1:
                y = 0
                flag = 0
            else:
                y += 1
    
    utente["Nickname"]= nick

    utente["Eta"]= int(input("Età: "))

    utente["Gender"]= input("Gender: ") 

    #chiediamo all'utente i suoi giochi preferiti e li inseriamo nel dizionario

    utente["Games"]= input("Inserisci i tuoi giochi preferiti separati dalle virgole: ")     

    lista.append(utente)
    
    #poi inseriamo i giochi preferiti degli utenti all'interno di una lista 
    #la split usa un elemento separatore (in questo caso la virgola) e li inserisce in una lista

    giochi= lista[i]["Games"].split(',')

    #print(type(giochi)) tipo: list


    #.strip() serve per eliminare gli spazi all'inizio di ogni stringa (gioco) che l'utente ha inserito

    for y in range(len(giochi)):
        giochi[y]= giochi[y].strip()


    #inserisco tutti i giochi in un unica lista

    for y in giochi:
        games.append(y)

    print("\n")




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




#qui stilo una classifica di tutti i giochi preferiti

diz_game= {}    #struttura dati: dizionario

for game in games:
    cont= 0
    if game in diz_game:
        diz_game[game]= diz_game[game] + 1
    else:
        cont += 1
        diz_game[game]= cont

print(f"Lista giochi: {diz_game}\n")






#passo i giochi ad un 'set' in modo che vengano eliminati i giochi presenti più di una volta

for x in games:
    g.add(x)


print(lista)
print("\nSET\n",g)




'''
Finita l'inserzione, creare un modulo statistico che analizzi i dati inseriti nel sistema.
In particolare si vuole sapere:
la percentuale di maschi e di femmine e la età massima, minima e media dei registrati.

'''
maschi=0
femmine=0
eta_max=0
eta_min=200
eta_media=0

n= len(lista)
for i in range(n):
    if lista[i]["Gender"] == "M":
        maschi += 1
    else:
        femmine += 1

    if lista[i]["Eta"] > eta_max:
        eta_max= lista[i]["Eta"]
    
    if lista[i]["Eta"] < eta_min:
        eta_min= lista[i]["Eta"]

    eta_media= eta_media + lista[i]["Eta"]

print("Percentuale di maschi registrati:", (maschi*100)/n)
print("Percentuale di femmine registrate:", (femmine*100)/n)
print("Utente con età maggiore:", eta_max)
print("Utente con età minore:", eta_min)
print("Età media degli utenti registrati:", eta_media/n)
    


