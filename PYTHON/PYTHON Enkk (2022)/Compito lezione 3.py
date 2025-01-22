#COMPITO 1 Lezione 03
#Creare per ogni compito e ogni soluzione un file.

## Compito 1
#Creare un programma che prenda in input dall'utente una serie di parole 
#o punteggiatura (sono ammessi solo `.` `,` `!` e `?`), una per volta. 
#L'inserzione si deve interrompere quando l'utente inserisce la 
#stringa "stop".

#Esempio di inserizioni (una ogni riga):
'''
ciao
come
stai
,
tutto
bene
?
sì 
grazie
stop
'''

lista= []
parola= input("Inserire una parola o una punteggiatura\n(sono ammessi solo `.` `,` `!` e `?`)\ne premere invio\n")

while parola != "stop":
    lista.append(parola)
    parola= input()

print(lista)




#Finita l'inserzione si stampi la serie di frasi risultante, andando 
#a capo dopo ogni frase (ossia dopo ogni '.' ',' '!' o '?'). 
#Assicurarsi che non vi siano spazi prima della `,`
#e che le maiuscole siano corrette. 

n= len(lista)

#elimino mediante .strip() eventuali spazi presenti all'inizio o 
#alla fine di ogni parola inserita

for i in range(n):
    lista[i]= lista[i].strip()

print(lista)


stringa= ""
#è già 1 perchè la prima parola rappresenta già l'inizio della frase
#quindi va scritta in maiuscolo
a_capo= 1 

for world in lista:
    if a_capo == 0 and world != ',':
        stringa= stringa + " " + world
    elif a_capo == 1:
        stringa= stringa + world.capitalize()
    else:
        stringa= stringa + world

    if world == ',' or world == '.' or world == '!' or world == '?':
        stringa= stringa + '\n'
        if world != ',':    #se il simbolo è la virgola, quando vado a capo il primo carattere della parola non deve essere maiuscolo
            a_capo= 1
        else:
            a_capo= 2
    else:
        a_capo= 0

print(stringa)







#Riportare poi un po' di statistiche in merito al testo, ed in particolare: 
'''
- Numero di parole ricevute (non si contino i segni di interpunzione)
- Numero di segni di interpunzione
- Numero di frasi 
- Il carattere più frequente
- Il carattere meno frequente
'''


#- Numero di parole ricevute (non si contino i segni di interpunzione)
#- Numero di segni di interpunzione
#- Numero di frasi

count_world=0
count_symbolize= 0

for world in lista:
    if world != ',' and world != '.' and world != '!' and world != '?':
        count_world += 1
    else:
        count_symbolize += 1


#LIST COMPREHENSION:
'''
this could also have been made with list comprehansion, taht can be learnt
in lesson 4. Example:

lista= ["ciao", ",", "come", "stai", "?", "bene"]

listcount= [world for world in lista if world != ',' and world != '.' and world != '!' and world != '?']

print(listcount)

#in questo modo listcount conterrà solo le parole esclusi i simboli {',' '.' '!' '?'}
'''

print("\nIl numero di parole inserite è:", count_world)
print(f"Il numero di segni di interpunzione sono: {count_symbolize}")
print(f"Il numero di frasi sono: {count_symbolize}")



#- Il carattere più frequente
#- Il carattere meno frequente

n= len(stringa)
count_max= 0
count_min= 1000

for i in range(n):
    count= 0
    if stringa[i] != " " and stringa[i] != "\n" and stringa[i] != ',' and stringa[i] != '.' and stringa[i] != '!' and stringa[i] != '?':
        for y in range(n):
            if stringa[i].lower() == stringa[y].lower():
                count += 1
    
        #cerca il carattere max e min e lo salva in una variabile
        if count > count_max:
            count_max= count
            carattere_piu_frequente= stringa[i].lower()
        
        if count < count_min:
            count_min= count
            carattere_meno_frequente= stringa[i].lower()

print(f"\nIl carattere più frequente è: {carattere_piu_frequente}")
print(f"\nIl carattere meno frequente è: {carattere_meno_frequente}")






#- Il carattere più frequente
#- Il carattere meno frequente
#mediante l'uso di un dizionario. La key è il carattere, mentre il valore è
#il numero di volte in cui il carattere compare nella stringa.

n= len(stringa)
count_max= 0
count_min= 1000
dict= {}
carattere_piu_frequente= []
carattere_meno_frequente= []
caratteri= set()

for i in range(n):
    count= 0
    
    if stringa[i] != " " and stringa[i] != "\n" and stringa[i] != ',' and stringa[i] != '.' and stringa[i] != '!' and stringa[i] != '?':
        if stringa[i] not in caratteri: #evita di ripetere il conteggio su caratteri che sono stati già contati
            caratteri.add(stringa[i])   #ogni carattere già contato viene salvato in un set()

            for y in range(n):
                if stringa[i].lower() == stringa[y].lower():
                    count += 1
        
            #se il carattere (key) non è presente nel dizionario, viene creata la nuova key, altrimenti se è già presente, la trova e gli aggiorna il valore.
            dict[stringa[i].lower()]= count 

            #cerca i valori max e min e li salva in due liste
            if count >= count_max:
                if count > count_max:
                    for index in range(len(carattere_piu_frequente)):
                        carattere_piu_frequente.pop()
                    carattere_piu_frequente.append(stringa[i].lower())
                elif count == count_max:
                    carattere_piu_frequente.append(stringa[i].lower())
                
                count_max= count
        
            if count <= count_min:
                if count < count_min:
                    for index in range(len(carattere_meno_frequente)):
                        carattere_meno_frequente.pop()
                    carattere_meno_frequente.append(stringa[i].lower())
                elif count == count_min:
                    carattere_meno_frequente.append(stringa[i].lower())
                
                count_min= count

print("\n",dict)
print(f"\nIl carattere più frequente è: {carattere_piu_frequente}")
print(f"\nIl carattere meno frequente è: {carattere_meno_frequente}")