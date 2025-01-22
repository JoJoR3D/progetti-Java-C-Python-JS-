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
