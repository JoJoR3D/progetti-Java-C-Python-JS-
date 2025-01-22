# # Compito 03 (off live)

# Creare una programma che prenda in input un file contenente due righe, 
# ciascuna rappresentante una lista di interi maggiori di `0`.

# Esempio di file:
# ```
# 2,1,3
# 3,1,5
# ```

# Le liste sono comma separated e di uguale lunghezza.

# Si generi dunque una matrice (una lista di liste) che abbia sulla 
#diagonale principale la somma delle due liste e in tutte le altre 
# posizioni `0`. Esempio:

# ```
# # sono estratte dal file
# l1 = [2,1,3]
# l2 = [3,1,5]

# Matrice risultante:

# 5 0 0
# 0 2 0 
# 0 0 8

# ```

# La matrice risultante deve essere stampata all'interno di un altro file.

# Si usino diversi metodi di supporto per organizzare appropriatamente 
# il programma (esempio, il caricamento da file, la generazione della 
# matrice, la stampa su file). 



#ESECUZIONE:

#scrivo sul file
'''
with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Compito_3_lez_4/file.txt", "w") as file:
    for i in range(6):
        s= input()
        file.write(s)
        if i == 2:
            file.write("\n")
'''


#leggo il file e inserisco i suoi valori in due liste
list1= []
list2= []
blocco= 0

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Compito_3_lez_4/file.txt", "r") as file:
    for read in file.read():
        #print(read)
        if read != ",":
            if read != "\n" and blocco == 0:
                list1.append(read)
            elif read == '\n':
                blocco= 1
            elif blocco == 1:
                list2.append(read)

print(list1)
print(list2)



#creo la matrice
list3= [[1]*len(list1),[1]*len(list2),[1]*len(list1)]  
righe= len(list3)   #lunghezza righe
colonne= len(list3[0])  #lunghezza colonne

index_i= 0
index_y= 0

for x in list1:
    for y in list2:
        if index_i == index_y:
            list3[index_i][index_y]= (int(list1[index_i]) + int(list2[index_y]))
        else:
            list3[index_i][index_y]= 0

        if index_y < colonne:
            index_y += 1            
    
    if index_i < righe:
            index_i += 1
            index_y= 0

print(list3)




#scrittura della matrice su un file
with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Compito_3_lez_4/matrice.txt", "w") as file:
    for i in range(len(list3)): #righe
        for j in range(len(list3[0])): #colonne
            file.write(str(list3[i][j])) #in un file di testo posso scrivere solo stringhe e non interi o altro che non sia testo
            file.write(" ") #dopo ogni numero, inserisco anche uno spazio
        file.write("\n")