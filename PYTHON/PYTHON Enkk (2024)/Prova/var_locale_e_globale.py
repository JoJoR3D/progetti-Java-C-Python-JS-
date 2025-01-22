x= 5		#Variabile globale

def ff():
#in alternativa invece di indicare che 'x' è una variabile globale, posso passarla come parametro della funzione 
  global x
  y= 5		#Variabile locale	
  x= x+1
  return x


print(ff())