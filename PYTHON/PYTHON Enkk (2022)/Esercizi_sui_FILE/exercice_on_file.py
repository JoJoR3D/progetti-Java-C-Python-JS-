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















exit(0)






#COMPITO 1
#Creare un programma che stampi la 4 riga di un file di testo chiamato: 'file_01.txt'

#qui leggo la riga 4 del file mediante un semplice contatore che conta 
#ogni volta che viene letta una nuova stringa del file  

#PERCORSO della cartella: indicando l'intero percorso prende il nome di 'path assoluto'    

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file_01.txt", "r") as file:
    cont=0
    for x in file:
        cont += 1
        #print(x,cont)
        if cont == 4:
            print(x)



#altro modo è usare readlines()

print("Altro modo:")
list= []

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file_01.txt", "r") as file:
    list= file.readlines()
    #print(list)
    
print(list[3])













#qui creo prima il file e ci scrivo dentro. La scrittura del file termina quando inserisco la stringa: "stop"
#se il file non è già presente, viene creato in automatico nel percorso inserito.
#se il file è già presente, quando ci scrivo viene sovrascritto,
#a meno che non scrivo partendo dall'ultima cosa inserita. Se non sbaglio bisogna usare invece di
#.write(), .append()

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file1.txt","w") as file:
    testo= input()
    file.write(testo)
    while testo != "stop":
        file.write("\n")
        testo= input()
        file.write(testo)


'''
altro modo per scrivere su file

file= open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file1.txt","w")
testo= input()
file.write(testo)
while testo != "stop":
    testo= input()
    file.write(input())

file.close()
'''

print("\n")

#qui leggo la riga 4 del file mediante un semplice contatore che conta 
#ogni volta che viene letta una nuova stringa del file

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2022)/Esercizi_sui_FILE/file1.txt", "r") as file:
    cont=0
    for x in file:
        cont += 1
        #print(x,cont)
        if cont == 4:
            print(x)









#------------------------------------------------------------------------------------------------------------------------------------
# FILE:

# Per ora ci siamo limitati a trattare dati in input presi da linea di comando, ma naturalmente è possibile elaborare
# dati presi da file presenti sul filesystem.


# leggere il contenuto di un file da python è semplicissimo:

f = open("demofile.txt", "r")
print(f.read())

# open è una funzione che prende come parametro il path del file (percorso) e la modalità di lettura
# la funzione read legge il file per intero e lo restituisce come stringa

# è possibile anche leggere il file riga per riga

f = open("demofile.txt", "r")
for x in f:
  print(x)


# terminata l'elaborazione del file è necessario chiuderne l'accesso con la funzione

f.close()

# per semplicità è anche possibile usare la keyword `with` che ci da accesso al file e lo chiude quando finisce il suo scope

with open('readme.txt', 'r') as f:
    f.read()

# la scrittura è altrettanto semplice
lines = ['writeme', 'How to write text files in Python']
with open('writeme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


# esistono anche altre funzioni che rendono la scrittura/lettura lievemente più comoda, come readlines() e writelines() che lavorano con liste di stringhe

# ecco degli esempi

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(lines)

lines = []
with open('readme.txt', 'r') as f:
    lines = f.readlines()

# Per sapere come trovare, definire e gestire i path dei file su vari OS: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f