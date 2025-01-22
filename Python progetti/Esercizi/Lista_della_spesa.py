'''
Lista della spesa:
Crea un programma che permetta all'utente di aggiungere, rimuovere e visualizzare gli elementi di una lista della spesa.
'''


# FUNCTION

# se un elemento non è presente nella lista della spesa, lo aggiunge e gli chiedo se si desidera sepcificarne la quantità,
# altrimenti gli assegno come valore 1.
# invese se un elemento è già presente, stessa cosa gli chiedo se si desidera sepcificarne la quantità,
# altrimenti gli incremento il suo attuale valore.
# il valore è inteso come quantità di quel oggetto.

def agg_lista(lista_spesa, oggetto):
    if oggetto not in lista_spesa:
        command= input("Si vuole specificare la quantità? SI o NO\n")
        if command.upper() == "SI":
            quantita= input("Indicarne la quantità\n")
            lista_spesa[oggetto]= int(quantita)
        else:
            lista_spesa[oggetto]= 1
    else:
        command= input("Si vuole specificare la quantità? SI o NO\n")
        if command.upper() == "SI":
            quantita= input("Indicarne la quantità\n")
            lista_spesa[oggetto]= lista_spesa[oggetto] + int(quantita)
        else:
            lista_spesa[oggetto]= lista_spesa[oggetto] + 1




# se un oggetto è già presente nella lista della spesa e se ha una quantità superiore a 1, chiedo se voglio diminuirne la quantità.
# se si indico di quanto diminuirne, se la quantità era 2 e lo diminuisco di 2, rimarrà 0 quindi l'elemento verrà eliminato.
# altrimenti se int(lista_spesa[oggetto]) non è > 1, la sua quantità è 1 allora lo elemina dalla lista della spesa.

def remove_lista(lista_spesa, oggetto):
    if oggetto in lista_spesa:
        if int(lista_spesa[oggetto]) > 1:
            command= input(f"L'elemento indicato è presente nella lista con una quantità di {lista_spesa[oggetto]}\nPremere 1 per ridurne la quantità, 2 per eliminarlo\n")
            
            if command == "1":
                quantita= input("\nIndicare di quanto diminuirne la quantità\n")
                
                if int(lista_spesa[oggetto]) - int(quantita) > 0:
                    lista_spesa[oggetto]= int(lista_spesa[oggetto]) - int(quantita)
                    print("Quantità diminuita!\n")
                else:
                    del lista_spesa[oggetto]
                    print("Elemento eliminato poichè la sua quantità è zero!\n")
            else:
                del lista_spesa[oggetto]
                print("Elemento eliminato con successo!\n")
        else:
            del lista_spesa[oggetto]
            print("Elemento eliminato poichè la sua quantità ora è zero!\n")
    else:
        print("L'elemento inserito non fa parte della lista della spesa\n")




# scive la lista della spesa sul file "Lista_spesa.txt"

def file_lista_spesa(lista_spesa):
    with open("C:/Users/Giuse/Desktop/Python progetti/Esercizi/Lista_spesa.txt", "w") as file:
        for key, value in lista_spesa.items():
            file.write(key)
            file.write(":")
            file.write(str(value))
            file.write("\n")




# ad ogni run del programma viene recuperata la lista della spesa dal file "Lista_spesa.txt"

def recupero_lista_spesa_da_file(lista_spesa):
    with open("C:/Users/Giuse/Desktop/Python progetti/Esercizi/Lista_spesa.txt", "r") as file:
        key= ""
        value= ""
        blocco= 0
        
        for object in file.readlines():
            for elem in object:
                #print(elem)
                if elem != ":" and blocco == 0:
                    key= key + elem
                elif elem != ":" and blocco == 1:
                    value= value + elem
                    blocco= 0
                    lista_spesa[key.strip("\n")]= int(value)
                    #print(lista_spesa)
                    key= ""
                    value= ""
                elif elem == ':':
                    blocco= 1






# MAIN

lista_spesa= {}

quest= input("Si desidera aggiungere un elemento alla lista della spesa? Scrivere SI o NO\n")


if quest.upper() == "SI":
    recupero_lista_spesa_da_file(lista_spesa)
    print(f"\nEcco la lista della spesa {lista_spesa}\n")

    new_object= input("Inserire l'elemento o gli elementi che si vogliono aggiungere alla lista della spesa\nUna volta terminato premere zero\n")
    while new_object != "0":
        if new_object != '0':
            agg_lista(lista_spesa, new_object)
                
        print("\n")
        new_object= input()


    file_lista_spesa(lista_spesa)
    print(f"\nLista della spesa aggiornata\n{lista_spesa}")

else:
    quest= input("\nSi desidera modificare la lista della spesa? Scrivere SI o NO\n")

    if quest.upper() == "SI":
        recupero_lista_spesa_da_file(lista_spesa)

        if len(lista_spesa) > 0:    
            new_object= input(f"\nEcco la lista della spesa {lista_spesa}\n\nIndicare l'elemento o gli elementi che si vogliono eliminare dalla lista\nUna volta terminato premere zero\n")

            while new_object != "0":
                if new_object != '0':
                    remove_lista(lista_spesa, new_object)
                
                new_object= input()


            file_lista_spesa(lista_spesa)
            print(f"\nLista della spesa aggiornata\n{lista_spesa}")
        else:
            print("\nLa lista della spesa è vuota!")

    else:
        print("\nArrivederci!")
