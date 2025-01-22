#COMPITO 2

# Compito 02 (in live)
# Creare una funzione che presi come parametri i path di 
# due file (`data/file_03_1.txt` e `data/file_03_2.txt`) 
# ne generi uno (`data/file_03_3.txt`) che contenga solo 
# le righe *comuni* fra i due file,  indipendentemente dalla loro posizione. 
# Nel file risultante le righe comuni dovranno apparire in ordine 
# inverso rispetto alla loro presenza nel file `data/file_03_1.txt`.

#copio in list il contenuto del file_03_01
list= []

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file_03_1.txt", "r") as file:
    #list= file.readlines()
    #LIST COMPREHENSION dell'istruzione sopra
    list= [word for word in file.readlines()]


#copio in list2 il contenuto del file_03_02
list2= []

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file_03_2.txt", "r") as file:
    #list2= file.readlines()
    #LIST COMPREHENSION dell'istruzione sopra
    list2= [word for word in file.readlines()]


#print(len(list),len(list2))

#creo il file: file_03_3, poi scorre le due list in ricerca degli elementi comuni e li salvo in reverse_list.
#poi mediante un for che parte dall'ultima posizione di reverse_list, scrivo il contenuto di reverse_list nel file: file_03_3
reverse_list= []
new_list= []

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file_03_3.txt", "w") as file:
    '''
    for i in range(len(list)):
        for y in range(len(list2)):
            if list[i].strip("\n") == list2[y].strip("\n"): #ogni parola nei due file ha anche l'accapo("\n"), con il .strip() lo elimino
                reverse_list.append(list[i])
                #file.write(list[i])
                break  
    '''
    #versione con LIST COMPREHENSION dei due cicli for annidati di sopra 
    #spiegazione: itero in list e in list2, e vedo se la word 
    #presa da list è uguale a quella presa da list2 (word2). 
    #Se lo è, allora la word viene inserita in reverse_list.
    #ogni parola nei due file ha anche l'accapo("\n"), con il .strip() lo elimino
    reverse_list= [word.strip("\n") for word in list for word2 in list2 if word.strip("\n") == word2.strip("\n")]

    #inserisco nel file il contenuto di reverse_list ma al contrario        
    #for i in range(len(reverse_list)-1,-1,-1):
    #    file.write(reverse_list[i]) 

    i= len(reverse_list)-1

    while i >= 0:
        file.write(reverse_list[i])
        i -= 1

    #inserisco in new_list tramite LIST COMPREHENSION la reverse_list al contrario
    new_list= [reverse_list[i] for i in range(len(reverse_list)-1,-1,-1)]


print(reverse_list)
print(new_list)