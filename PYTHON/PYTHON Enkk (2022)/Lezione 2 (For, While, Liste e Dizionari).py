#CICLO WHILE:

print("Esercizio 1")
condition= True

while condition:
    print("Ciao!\n")
    condition= False




print("Esercizio 2")
cont= 0

while cont < 10:
    print(cont)
    cont += 1




print("\nEsercizio 3")

print("---Login casino---\n")
nome= input("Inserire il proprio nome:\n")
cognome= input("Inserire il proprio cognome:\n")
eta= input("Inserire la propria età:\n")
#flag= 0

while len(nome) <= 1 or len(cognome) <= 1: #flag == 0:

    if len(nome) > 1 and len(cognome) > 1 and int(eta) >= 18:
        print("\nAccesso consentito!")
        #Print a string of confirm if first letter of name and surname is uppercase
        print(f"\nNome: {nome.capitalize()}\nCognome: {cognome.capitalize()}\nEtà: {eta}")

        #flag= 1

    elif len(nome) <= 1:
        print("\nAccesso negato! La lunghezza del nome deve essere maggiore di 1")
        nome= input("Reinserire il proprio nome:\n")

    elif len(cognome) <= 1:
        print("\nAccesso negato! La lunghezza del cognome deve essere maggiore di 1")
        cognome= input("Reinserire il proprio cognome:\n")

    elif int(eta) < 18:
        print("\nAccesso negato! Solo i maggiorenni possono accedere alla piattaforma")
        #flag= 1

    else:
        print("\nAccesso negato! Nome e Cognome devono avere lunghezza maggiore di 1")
        nome= input("Inserire il proprio nome:\n")
        cognome= input("Inserire il proprio cognome:\n")



if int(eta) < 18:
    print("\nAccesso negato! Solo i maggiorenni possono accedere alla piattaforma")
else:
    print("\nAccesso consentito!")
    print(f"\nNome: {nome.capitalize()}\nCognome: {cognome.capitalize()}\nEtà: {eta}")






print("\nEsercizio 3: Dizionario e Liste")

print("\nLISTE")

sub_list= ["carlo", "pietro", "luca", "renzo", "lucia"]

print(sub_list)
print(len(sub_list))
print(sub_list[3])

sub_list[0]= "gianluca"
print(sub_list)

cont= 0
while cont < len(sub_list):
    print(sub_list[cont])
    cont += 1

#Stesso esercizio del while però applicato mediante il for

for x in sub_list:
    print(x)







#ESERCIZIO
#dichiarare due liste di numeri con cinque elementi ciascuna
#creare una lista concatenata che includa entrambe
print("\nESERCIZIO:")

lista1= [0,1,2,3,4]
lista2= [5,6,7,8,9]

lista3= lista1 + lista2
print(lista3)

new_list= []
for x in lista1 + lista2:
    new_list.append(x)

print("new_list:", new_list)



#scrivere un programma che restituisca la somma degli elementi di due liste di uguale lunghezza
print("\nscrivere un programma che restituisca la somma degli elementi di due liste di uguale lunghezza")
if len(lista1) == len(lista2):
    somma= 0
    for i in lista1 + lista2:
        somma= somma + i
    print(f"Somma: {somma}")
else:
    print("\nLe due liste hanno una lunghezza diversa")




#scrivere un programma che sommi due liste di uguale lunghezza
print("\nscrivere un programma che sommi due liste di uguale lunghezza")
list= []

if len(lista1) == len(lista2):
    somma= 0
    for i in range(len(lista1)):
        print(i)
        list.append(lista1[i] + lista2[i])
    print(f"List: {list}")
else:
    print("\nLe due liste hanno una lunghezza diversa")










print("\nDIZIONARI")
#i dizionari sono liste che contengono la coppia: chiave\valore

nick= {"nome": "Enrico", "nickname": "Enkk"}

#accedere al valore indicando la chiave
print("\naccedere al valore indicando la chiave")
print(nick["nome"])

#modificare il valore di una chiave
print("\n#modificare il valore di una chiave")
nick["nome"]= "Filippo"
print(nick["nome"])

#creare una nuova chiave e un nuovo valore
print("\ncreare una nuova chiave e un nuovo valore")
nick["eta"]= 32
print(nick)

#per vedere le chiavi di un dizionario si usa .keys()
print("\nper vedere le chiavi di un dizionario si usa .keys()")
print(nick.keys())

#per vedere i valori di un dizionario si usa .values()
print("\nper vedere i valori di un dizionario si usa .values()")
print(nick.values())

#per vedere la coppia chiave\valore di un dizionario si usa .items()
print("\nper vedere la coppia chiave\valore di un dizionario si usa .items()")
print(nick.items())

#per vedere se una chiave è presente nel dizionario si usa 'in'
print("\nper vedere se una chiave è presente nel dizionario si usa 'in'")
print("nickname" in nick.keys())

#lo stesso per vedere se un valore è presente nel dizionario si usa 'in'
print("\nper vedere se una chiave è presente nel dizionario si usa 'in'")
print("Enkk" in nick.values())

#ciclo for per stampare la coppia chiave\valore di un dizionario
print("\nciclo for per stampare la coppia chiave-valore di un dizionario")
for key,value in nick.items():
    print(key)
    print(value)


#Esempio di accesso a un file .json che non è altro che un insieme di liste e dizionari
#print(x["ilmessageroit"][0]["text"])
#print(x["ilmessageroit"][1]["hashtags"][0])








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