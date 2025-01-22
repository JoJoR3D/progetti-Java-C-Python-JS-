#Esercizio 004
#Generatore di Password
#Scrivi una funzione generatrice di password.

#La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, e di 20 caratteri ASCII qualora desideri una password più complicata.

#FUNZIONE

import random

def password(ordine):
  i= 0
  caratteri= ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
            "l", "m", "n", "o", "p", "q", "r", "s", "t", 
            "u", "v", "z"]
  ASCII= ["$","%","&","/","(","=","?","^","+","*"]
  numeri= ["0","1","2","3","4","5","6","7","8","9"]
  
  n_caratteri= len(caratteri)
  n_ASCII= len(ASCII)
  n_numeri= len(numeri)

  passw= []
  
  if ordine == 0:
    while i < 8:
      scelta= random.choice(range(0,2))
      if scelta == 0:
        c= random.choice(range(0,n_caratteri-1))
        passw.append(caratteri[c])
      else:
        n= random.choice(range(0,n_numeri-1))
        passw.append(numeri[n])

      i += 1
        
  elif ordine == 1:
    while i < 20:
      scelta= random.choice(range(0,3))
      if scelta == 0:
        c= random.choice(range(0,n_caratteri-1))
        passw.append(caratteri[c])
      elif scelta == 1:
        n= random.choice(range(0,n_numeri-1))
        passw.append(numeri[n])
      elif scelta == 2:
        a= random.choice(range(0,n_ASCII-1))
        passw.append(ASCII[a])

      i += 1


  p= "".join(passw)
  return p


#MAIN
scelta= input("Generatore di password. Selezionare 0 per una password semplice, 1 per una password più complicata\n")

num_scelta= int(scelta)

parola_ordine= password(num_scelta)
print(parola_ordine)