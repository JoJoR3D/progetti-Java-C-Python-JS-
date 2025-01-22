'''
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
La classe dovrà avere i seguenti metodi:
Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.
'''

class GestoreMagazzino:
    prodotti= {}
    costo_magazzinaggio= 0.0

    def __init__(self, prodotti, costo_magazzinaggio):
        self.prodotti= prodotti
        self.costo_magazzinaggio= costo_magazzinaggio



class Prodotto(GestoreMagazzino):   # la classe Prodotto sta ereditando metodi e altro dalla classe GestoreMagazzino
    nome= ""
    prezzo= 0
    scorta= 0

    def __init__(self, nome, prezzo, scorta):
        self.nome= nome
        self.prezzo= prezzo
        self.scorta= scorta


    def aggiungi_prodotto(self):
        p= Prodotto(self.nome, self.prezzo, self.scorta)
        p.prodotti[self.nome]= self.scorta
        print(p.prodotti)

    def rimuovi_prodotto(self):
        p= Prodotto(self.nome, self.prezzo, self.scorta)
        del p.prodotti[self.nome]   
        print(p.prodotti)  

    def calcola_costi_magazzinaggio(self):
        p= Prodotto(self.nome, self.prezzo, self.scorta)

        for value in p.prodotti.values():
            p.costo_magazzinaggio= p.costo_magazzinaggio + (int(value) * 1.5)   # il costo del magazzinaggio poichè la traccia non specifica come calcolarlo, l'ho inventato io.
            print(f"Costo magazzinaggio a fine mese: {p.costo_magazzinaggio}")
        






# MAIN

x= Prodotto("Svelto", "3", "2")
y= Prodotto("Nutella", "5", "3")

x.aggiungi_prodotto()
y.aggiungi_prodotto()
x.calcola_costi_magazzinaggio()

print("\n")

x.rimuovi_prodotto()
x.calcola_costi_magazzinaggio()












exit(0)












# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” 
# che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.


class Impiegato:
    nome= ""
    cognome= ""
    matricola= 0
    stipendio= 0

    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome= nome
        self.cognome= cognome
        self.matricola= matricola
        self.stipendio= stipendio

    def aumenta_stipendio(self):
        self.stipendio= self.stipendio + ((self.stipendio*10)/100)  # aumenta lo stipendio del 10%

    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola: {self.matricola}, stipendio: {self.stipendio}")   # stampa tutti i dettagli



# MAIN

impiegato= Impiegato("Mario", "Rossi", 12345, 3000)

impiegato.aumenta_stipendio()

impiegato.stampa_dettagli()






exit(0)









# Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. 
# Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.


class Automobile:
    marca= ""
    modello= ""
    anno= 0

    def __init__(self, marca, modello, anno):
        self.marca= marca
        self.modello= modello
        self.anno= anno

    def descrivi(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")



# MAIN    

automobile= Automobile("Toyota", "Corolla", 2017)
automobile.descrivi()






exit(0)








# Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.


class Animale:
    nome= ""
    specie= ""

    def __init__(self, nome, specie):
        self.nome= nome
        self.specie= specie

    def emetti_suono(self):
        if self.specie == "gatto":
            print(f"{self.nome}... Miao!")
        
        elif self.specie == "cane":
            print(f"{self.nome}... Bau!")

        else:
            print(f"{self.nome}... Verso animale non troato")




# MAIN

animale= Animale("Venere", "gatto")
animale_2= Animale ("Max", "cane")
animale_3= Animale("Leo", "giraffa")

animale.emetti_suono()
animale_2.emetti_suono()
animale_3.emetti_suono()








exit(0)







# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.


class Persona:
    nome= ""
    eta= ""
    
    def __init__(self, nome, eta):
        self.nome= nome
        self.eta= eta
          
    def presentazione(self):
        print(f"Ciao mi chiamo {self.nome} e ho {self.eta} anni")




# MAIN

persona= Persona("Marco", "32")

persona.presentazione()

        



