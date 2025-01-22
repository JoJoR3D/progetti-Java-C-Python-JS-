# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.



# FUNCTION 

def word_palindrome(lista):
    l= []

    for parola in lista:     # Prendo la parola dalla lista.
        check= invertire_parola(parola) # Controllo per vedere se la parola è palindroma. Se lo è la function invertire_parola mi ritorna 1.

        if check == 1:      # Se la function invertire_parola mi ritorna 1, allora salvo la parola palindroma nella lista "l".
            l.append(parola)

    return l




def invertire_parola(parola):
    stringa= ""

    for i in range(len(parola)-1, -1, -1):  # Inverto la parola passata alla function facendo un ciclo for al contrario sulla parola e assegnandola a un stringa.
        stringa= stringa + parola[i]

    if stringa == parola:   # Se la parola invertita è uguale alla parola data in input, vuol dire che la parola data in input è palindroma e allora ritorno 1.
        return 1
    else:
        return 0
    




# MAIN

lista= ["luca", "anna", "cozza", "scoglio", "otto"]

ll= word_palindrome(lista)

if len(ll) > 0:
    print("Ecco le parole palindrome presenti nella lista data in input:", ll)
else:
    print("La lista data in input non ha parole palindrome")