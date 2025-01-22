#Variabili

#python non è un linguaggio fortemento tipato, non c'è bisogno di indicare il tipo delle variabili, lo capisce dal valore che assegniamo alla variabile
a= 1
print(a)



print("________\n\n")

#concatenazione tra stringhe
s= "Ciao"
v= " "
p= "Mondo" 

string= s+v+p

print(string)

print(len(string))



print("________\n\n")

#elevazione a potenza
a= 4**2
print("Potenza con base 2 di 4:", a)


#N.B. python non ha il tipo char (carattere)



print("________\n\n")

#Valori BOOLEANI

a= True
b= False

c= a and b
print(c)

c= a or b
print(c)

c= not b
print(c)

f= 10
g= f > 5
print(g)

c= not(a and b)
print(c)

c= (a and b) or (a and b)
print(c)

c= (a and b) or (a or b)
print(c)







print("________\n\n")

#COSTRUTTO DI SELEZIONE

print("Costrutto di selezione:\n")

a= True
b= False

if b:
    print("ramo vero")
else:
    print("ramo falso")









print("________\n\n")

#Input da tastiera

print("INPUT da tastiera\n")

valore= input("Dammi un dato\n")
print(valore)

x= input("Dammi un numero\n")
y= input("Dammi un altro numero\n")
z= int(x)**int(y)
print("Risultato: " + str(z)) #concatenazione tra stringhe



#altro modo per commentare oltre all'asterisco è il triplo apice:

'''

Commento

'''



#COMPITO lezione 1

#Creare uno script di python che simuli il login ad un sito di casinò
#Si chieda all'utente nome cognome ed età. Si verifichi che il nome e il cognome sia più lungo di un carattere e che l'età sia maggiore o uguale a 18 anni.
#Se tutto è corretto stampare una stringa di conferma altrimenti comunicare l'errore all'utente.
#Si consideri che l'utente fornià sempre dati di tipo corretti.

#Stampare il resocondo dei dati assicurandoci che l'utente abbia inserito nome e cognome che cominciano con la maiuscola. 



