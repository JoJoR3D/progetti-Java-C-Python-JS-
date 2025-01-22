# Scrivi una funzione in Python che prende due stringhe, conta il numero di volte che ogni stringa contiene gli stessi tre caratteri allo stesso indice. 
# Stampa l’output.

# FUNCTION

# Stessa function dell'esercizio precedente, ma qui i tre caratteri di s1 devono essere uguali e trovarsi alla stessa posizione (indici) dei tre caratteri di s2.

def sottostringa(s1, s2):

    cont_s1= 0
    cont_s2= 0
    i= 0
    y= 0
    indice= 0
    flag= 0
    under_string= ""
    stringa1= ""
    stringa2= ""

    while i < len(s1):
        stringa1= stringa1 + s1[i]
        cont_s1 += 1
        i= i+1

        if cont_s1 == 3:            
            print("Stringa 1:", stringa1)

            y= i - cont_s1  # in questo modo prendo i tre caratteri di s2 presenti alla stessa posizione dei tre caratteri di s1 e poi li confronto.
            n= y + cont_s1  # 'y' è il punto di inizio del ciclo, 'n' il punto di fine.
            print(f"y: {y}, n: {n}")

            while y < n and y < len(s2):
                stringa2= stringa2 + s2[y]
                cont_s2 += 1
                y= y+1
                
                if cont_s2 == 3:
                    print("Stringa 2:", stringa2)

                    if stringa1 == stringa2:
                        flag= 1
                        indice= indice + i - 3
                        under_string= under_string + stringa1
                    else:
                        stringa2= ""
                        cont_s2= 0

            if flag == 1:
                break
            else:
                stringa1= ""
                stringa2= ""
                under_string= ""
                i= i-2
                cont_s1= 0
                cont_s2= 0
                indice= 0

        
        y= 0
        
    if under_string != "" :
        print(f"\nUNDER STRING: {under_string} a partire dall'indice {indice}")
    else:
        print("\nNon esiste nessuna sottostringa corrispondente tra le due stringhe")




# MAIN

stringa1= "feapjefgemfgpoejovarejepovj"
stringa2= "dafqweorifeovjepokarefoejff"

sottostringa(stringa1, stringa2)



















exit(0)












# Scrivi una funzione in Python che prende due stringhe, conta il numero di volte che ogni stringa contiene gli stessi tre caratteri. 
# Stampa l’output.

# FUNCTION

def sottostringa(s1, s2):

    cont_s1= 0
    cont_s2= 0
    i= 0
    y= 0
    under_string= ""
    stringa1= ""
    stringa2= ""
    flag= 0

    while i < len(s1):
        stringa1= stringa1 + s1[i]      # creo la sottostringa della s1 di 3 caratteri
        cont_s1 += 1
        i= i+1

        if cont_s1 == 3:
            print("Stringa 1:", stringa1)

            while y < len(s2):          # creo la sottostringa della s2 di 3 caratteri
                stringa2= stringa2 + s2[y]
                cont_s2 += 1
                y= y+1
                
                if cont_s2 == 3:
                    print("Stringa 2:", stringa2)

                    if stringa1 == stringa2:    # Se le due sottostringhe concidono le assegno alla stringa "under_string" e pono il flag a 1
                        flag= 1
                        under_string= under_string + stringa1
                    else:                       # altrimenti prendo i successivi 3 caratteri della s2 e li confronto con quelli presei in precedenza da s1. Continuo fino al termine di s2. Poi riparto prendendo i successivi tre caratteri della stringa s1.
                        stringa2= ""
                        cont_s2= 0
                        y= y-2

            if flag == 1:
                break
            else:
                stringa1= ""
                stringa2= ""
                under_string= ""
                i= i-2
                cont_s1= 0
                cont_s2= 0
        
        y= 0
        
    print("\nUNDER STRING:", under_string)




# MAIN

stringa1= "camminare"
stringa2= "fumare"

sottostringa(stringa1, stringa2)











exit(0)









# Scrivi una funzione Python per rimuovere i duplicati da una lista preservando l’ordine degli elementi al suo interno.

# FUNCTION

def delete_double(lista):

    cont_l1= -1
    cont_l2= -1

    for l1 in lista:    # ciclo esterno
        cont_l1 += 1
        
        for l2 in lista:    # ciclo interno
            cont_l2 += 1
            
            if cont_l1 != cont_l2:      # per evitare che vengano confrontate due parole presenti alla stessa posizione. Ad esempio, al primo ciclo, l1 punta alla poszione 0 così come l2. Il confronto non viene eseguito perchè puntano alla stessa parola nella medesima posizione.
                if l1 == l2:
                    lista.pop(cont_l2)  # pop è un metodo delle liste per eliminare un elemento dalla lista passandogli l'indice (Per questo gli passo cont_l2).

        cont_l2= -1






# MAIN

lista= ["mela", "pera", "banana", "mela", "caffé", "banana"]

print("Prima:", lista)

delete_double(lista)

print(f"Dopo: {lista}")















exit(0)









# Scrivi un programma Python per trovare quattro numeri interi pari positivi la cui somma è un dato numero intero. Esempio – input: n = 100 output: [94,2,2,2]


import random
import time


# FUNZIONI

def find(numero):
    lista= []
    somma= 0
    cont= 0
    cont_cicli= 0
    num= numero

    while somma != numero:
        while cont < 4 and somma <= numero:
            if numero - somma >= 90:
                detrattori= random.randint(90,100)
                print(detrattori)
            elif numero - somma >= 50 and numero - somma < 90:
                detrattori= random.randint(50,89)
                print(detrattori)
            elif numero - somma >= 25 and numero - somma < 50:
                detrattori= random.randint(25,49)
                print(detrattori)
            elif numero - somma >= 10 and numero - somma < 25:
                detrattori= random.randint(10,24)
                print(detrattori)
            elif numero - somma >= 0 and numero - somma < 10:
                detrattori= random.randint(0,9)
                print(detrattori)

            
            if detrattori%2 == 0 and detrattori != 0: 
                num = num - detrattori
                somma= somma + detrattori
                lista.append(detrattori)
                cont += 1
            else:
                cont_cicli += 1

            if cont_cicli == 500:
                break

        if somma != numero:
            print("Somma: ",somma)
            time.sleep(0.5)
            lista= []
            somma= 0
            cont= 0
            cont_cicli= 0
            num= numero
            print("\n\nNUOVO CICLO")

    return lista




def controllo(numero):
    if numero%2 == 0:
        return 0
    else:
        return 1






# MAIN

numero= input("Inserire un numero intero pari\n")
control= controllo(int(numero))

if control == 0:
    l= find(int(numero))
    print(l)
else:
    print("Errore nel numero inserito!")












exit(0)







# Scrivi un programma in Python per estrarre valori da un dizionario noto e crea una lista di liste da questi valori.



# FUNCTION

def estrattore_valori(dizionario):

    lista= []

    for chiave, valore in dizionario.items():
        chiave= []

        for v in valore:
            chiave.append(v)
        
        lista.append(chiave)

    return lista






# MAIN

diz= {"frutta": ["banana", "mela", "pera"], "verdura": ["insalata", "zucchine", "pomodoei"], "dolce": ["tiramisù", "sorbetto", "gelato"]}

l= estrattore_valori(diz)

print(l)

