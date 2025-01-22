#Esercizio 023
#Testi di canzoni
#Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.

#Suggerimento: dovrai utilizzare l'istruzione with.





#FUNZIONE:

def funz(titolo, testo):
	nome_file= titolo + ".txt"
	with open(nome_file, "w") as file_testo:
		file_testo.write(testo) 

	#CONTROLLO PER VERIFICARE SE IL FILE E' STATO CHIUSO CORRETTAMENTE
	print(file_testo.closed)
	




#MAIN:

titolo= input("Inserire il titolo della canzone:\n")
testo= input("Inserire il testo della canzone:\n")
file= open("titolo_canzone.txt", "w")


#CHIAMATA FUNZIONE
funz(titolo,testo)


#LETTURA DEL FILE CREATO
nome_file= titolo + ".txt"
file= open(nome_file, "r").read()
print(file)	

		

