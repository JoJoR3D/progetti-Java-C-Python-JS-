'''
SITO PER VEDERE COSA ACCADE NELLA ZONA DI MEMORIA QUANDO ESEGUIAMO
UN CODICE:
https://pythontutor.com/render.html#mode=display

'''

#Python ha due zona di memroia: heap e stack.
#Funzionano in modo diverso.

#STACK
#Nello stack i dati vanno inseriti dal basso verso l'alto (pila).
#Di questa pila ci sono zone non accessibili (frame di attivazione).
#Quando c'è un frame specifico nella pila, il programma può accedere solo
#alle variabili di quel frame e non a tutto il resto
#Le variabili nello stack possono puntare a delle zone di memoria nell'heap.

#PROGRAM COUNTER
#Instructoin pointer (o Program counter) memorizza la posizione
#della prossima istruzione che il programma deve eseguire.

#Stack / Heap
#Quando dichiariamo e inizializziamo una lista, nello stack viene memorizzato
#l'indirizzo di memoria (puntatore) nel quale sono presenti gli elementi 
#della lista (HEAP è la zona di memoria che contiene gli elementi della
#lista)
#Questo perchè lo stack non può contenere tutti gli elementi nella lista,
#in esso viene memorizzato la variabile lista che contiene il PUNTATORE 
#che è l'indirizzo di memoria nel quale sono memorizzati glie elementi
#della lista.


#NOTA BENE:
#In python di solito nello stack si trovano solo le variabili primitive: 
#int,double e boolean. Tutte le altre finiscono nell'heap (lo stack contiene
#il puntatore ovvero l'indirizzo di memoria di dove, ad esempio, gli elelìmenti
#di una lista sono contenuti nell'heap).

#Nota bene:
#lista= ["penna","quaderno"]
#lista2= ["casa","giardino"]
#lista= lista2

#In questo caso nello stack viene creata la variabile lista che contiene
#un puntatore all'area di memroia heap nel quale sono contenuti gli elementi
#di lista. Lo stesso accade per lista2.
#Però quando vado ad assegnare a lista la lista2, nello stack lista ora conterrà
#un puntatore all'area di memroia heap nel quale sono contenuti gli elementi
#di lista2. Quindi lista e lista2 punteranno alla stessa area di memoria
#dell'heap.
#Quindi se, ad esempio, lista va a modificare qualche cosa, in automatico 
#la stessa modifica viene vista anche da lista2 perchè entrambe 
#puntano algi stessi elementi. 
#Ma cosa succede agli elementi che puntava lista (["penna","quaderno"])??
#La zona di memria dell'heap che li contiene non è più indirizzata, quindi
#nessuno gli potrà accedervi. Dopo un pò viene ripulita da un altro processo 
#che gira e che riutilizzera quella zona di memoria.
#Ad esempio in java, questo processo di pulizia della zona di memoria non
#indirizzabile viene eseguita da un processo che si chiama "Garbage collection".




# CONTINUO IN LEZIONE 7

'''
Funzioni nello stato della memoria
Quando dichiariamo un metodo, di solito si usa dichiararle all'inizio
del codice, la dichiarazione viene salvata nello stack e contiene un 
puntatore (indirizzo) alla funzione salvata nell'heap.
In questo modo quando viene chiamata la funzione nel main, l'interprete 
sa in che zona di memoria andare a cercarla.

Quando il codice viene eseguito e viene chiamato il metodo, l'interprete
trova la zona di memoria dove è stato salvato la dichiarazione del metodo,
poi alloca nello stack una porzione dedicata all'esecuzione del metodo
e delle sue variabili locali.
Al termine dell'esecuzione del metodo, l'allocazione del metodo nello 
stack viene eliminata e con essa tutte le sue variabili locali, le quali
saranno perse per sempre.

N.B. le funzioni sone quelle non di CLASSE, mentre i metodi sono funzioni
     di classe (oggetti)


PASSAGGIO DEI PARAMETRI PER VALORE O PER RIFERIMENTO
Passaggio per valore significa passare una copia della variabile 
al metodo. 
Passaggio per riferimento significa passare l'accesso alla variabile 
al metodo. Di conseguenza con il passaggio per riferimento, qualsiasi
cambiamento della variabile nel metodo comporta anche ad un cambiamento
della variabile fuori dal metodo.

Esempio passaggio per VALORI:

def sommetta(a,b):
	c = a+b
	a = 100
	b = 150
	return c

a = 10
b = 15
c = sommetta(a,b)

Al metodo sommetta passo per valore il valore delle variabili 
'a' e 'b'. Le modifiche a tali valori nel metodo non influenzano il valore
delle variabili (globali) 'a' e 'b' fuori dal metodo.





Esempio passaggio per RIFERIMENTO:

l1 = [1,2,3]
l2 = [10,20,30]

# look at the parameters!

def sommetta(l1,l2):
	l3 = [0]*len(l1)
	for i in range(len(l1)):
		l3[i]	= l1[i]+l2[i]

	return l3

lresult = sommetta(l1,l2)
print(lresult)

Al metodo sommetta passiamo l1 e l2 (liste) che sono memorizzate 
nello stack e contengono un puntatore (indirizzo) ciascuna alle due
liste memorizzate nell'heap.
Quindi a sommetta passiamo due puntatori alle due liste. Quindi sommetta
opererà direttamente sulle due liste e se le modificherà, poichè vi
lavora direttamente, andrà a modificare l1 e l2 dichiarate fuori dal
metodo (però non è questo il caso). 
Al termine del metodo viene ritornata una nuova lista, l3, che viene 
aggiunta allo stack sotto il nome di 'lresult' che conterrà un 
puntatore (indirizzo) alla lista memorizzata nell'heap ([11,22,33]).


'''