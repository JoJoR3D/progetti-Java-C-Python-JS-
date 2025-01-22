#IMPORT

# La maggiorparte delle cose che vorrete fare sarà già stata fatta.

# Per questo motivo prima di iniziare un grande progetto conviene *sempre* googlare e trovare soluzioni altrui.

# Se siamo fortunati, parte del nostro problema non solo è già stato risolto e ne troviamo il codice,
# ma quel codice è anche stato debitamente impacchettato, distribuito e noi dobbiamo solo *importarlo* nel codice.

# python (come ogni linguaggio di programmazione) ci permette di fare questo tramite il comando

#import NOME

# dove NOME corrisponde al modulo o pacchetto che vogliamo importare, comprensivo delle sue funzionalità.

# Sarebbe necessario fare una distizione precisa fra moduli e pacchetti, ma per semplicità diciamo semplicemente che i pacchetti contengono multipli moduli.

# alcuni pacchetti sono già inclusi dentro python quando lo installiamo, quindi ci basterà davvero solo fare l'import per poter usare
# le funzionalità nel nostro codice

# se invece il pacchetto dovesse essere esterno, da terminale possiamo installarlo. Ci sono tanti modi per installare pacchetti da internet,
# si suggerisce di usare "pip" (package installer for python), che dovreste già aver installato.

# da terminale potete dare

# pip install nome_pacchetto

# e poi eseguire l'import senza problemi.

# Il sito web https://pypi.org/project/pip/ offre una miriade di pacchetti, e in alto trovate il comando da dare (il nome del pacchetto necessario)

# ogni pacchetto poi presenterà le sue "istruzioni" (detta documentazione) su come usare le funzionalità.

# Le funzionalità di import non si limitano soltanto a pacchetti/moduli esterni ma possono (e devono) essere usate anche per importare le nostre funzionalità
# che magari abbiamo implentato in altri file

# se il file `uno.py` si trova nella stessa cartella del file `due.py` potremo importare il primo nel secondo usando semplicemente

# import uno

# Il tema degli import e dei packages è piuttosto complicato, quindi non ci addentriamo troppo.
# Per poterne parlare dignitosamente dovremmo anche introdurre il concetto di oggetti e classi che per ora è troppo avanzato.

# Lascio comunque un link https://realpython.com/python-import/ che fornisce una spiegazione completa e dettagliata









#LIST COMPREHENSION

# Le liste sono una struttura dati usatissima per fare un sacco di cose. 
# Capita dunque molto spesso di dover scorrere una lista soltanto per verificare una condizione, o prendere un elemento, ecc.

# Per questo motivo python offre uno zucchero sintattico chiamato list comprehension (LC in breve) che permette di creare una nuova lista 
# a partire da una esistente in maniera più rapida (dal punto di vista sintattico) e leggibile.

# Vediamo subito un esempio. Diciamo di avere una lista di frutti e voler prendere tutti quelli che contengono la lettera 'a'. 
# Con le nozioni che abbiamo, dovremmo scrivere:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# ma usando invece le LC:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] # questa è la list comprehension

print(newlist)

# il for è stato ridotto ad una riga sola, ed è anche più leggibile!

# la sintassi generica di una LC è la seguente:

"""
newlist = [expression for item in iterable if condition]
"""

# dove: 
# - newlist è la variabile che contiene la nuova lista
# - iterable è la lista (in realtà una qualunqe struttura dati iterabile) dalla quale partiamo
# - item è il singolo elemento della lista
# - condition è la condizione che viene testata, ed è opzionale
# - expression è una espressione che produrrà il nuovo elemento che verrà inserito in newlist

# vediamo un po' di esempi:

newlist = [x for x in fruits if x != "apple"] # prende solo gli elementi che non sono apple

newlist = [x for x in fruits] # prende ogni x nella lista, senza condizione. quindi li prende tutti e di fatto duplica la lista di partenza

newlist = [x for x in range(10)] # lista di valori da 0 a 9

newlist = [x for x in range(10) if x < 5] # come sopra, ma i valori accettati sono solo quelli minori di 5


# come accennato l'expression può contenere delle manipolazioni prima di fornire l'elemento che farà parte della nuova lista

newlist = [x.upper() for x in fruits] # tutti i frutti in maiuscolo

# possiamo anche creare cose più complicate, come ad esempio:

newlist = [x if x != "banana" else "orange" for x in fruits]

# che significa resitutisci il frutto se questo non è banana, altrimenti se è banana restituisci orange
# l'if e l'else sono legati a 'x', cioè fanno parte del expression
# se l'if ha anche la condizione else, allora l'if e l'else fanno parte del expression e vanno inserite prima del for,
#altrimenti se vi è la sola condzione dell'if, la condizione del if non fa parte del expression e va inserita dopo il ciclo for.




# Le comprehension non esistono solo per le liste, ma anche per altre collezioni. 
# Per semplicità non le introduciamo, ma qui ci sono degli esempi: https://www.geeksforgeeks.org/comprehensions-in-python/ 












#FILE

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