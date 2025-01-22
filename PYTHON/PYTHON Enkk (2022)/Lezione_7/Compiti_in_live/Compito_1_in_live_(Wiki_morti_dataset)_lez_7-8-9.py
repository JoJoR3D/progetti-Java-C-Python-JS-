'''
Lezione 7

Progetto "Parsing Wikipedia: il wikimorti dataset"
Creare un semplice programma che costruisca un database (in formato json) 
di tutte le morti illustri dal 1992 al 2021. 
Salvare il file in data/deadge.json. 
Il database dovrà contenere:

Data di morte
Nome e cognome del deceduto
Età del deceduto
Se possibile anche altri dati relativi alla morte (laddove ci siano 
consistenze).

Questo database sarà poi usato nei prossimi compiti.

Ottenere questi dati utilizzando le API di Wikipedia (interrogabili 
tramite questo pacchetto). In particolare si osservi come sono costruite 
queste pagine e trovare l'algoritmo di esplorazione delle pagine più 
efficente ed automatizzato. 
Ecco alcune pagine interessanti per il compito:

https://en.wikipedia.org/wiki/Lists_of_deaths_by_year
https://en.wikipedia.org/wiki/1990#Deaths


Il compito è stato iniziato in live e continuerà nella prossima lezione. 
Pertanto, niente compiti a casa!

'''








import wikipediaapi
import json

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI)

#page_py = wiki_wiki.page("Deaths_in_May_1989")
#print(page_py.text)



def check_exists(wiki_wiki, stringa):
    page_py = wiki_wiki.page(stringa)
    print(stringa, page_py.exists())

    #con .exists() controllo se le pagine web presenti in page_name
    #esistono oppure no
    if page_py.exists() == "False":
        page_false.append(stringa)





months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#dal 1987 in poi le strutture delle pagini sono uguali. 
#Prima del 1987 hanno quasi tutte una struttura diversa. 
#Quindi ci vorrebbe un codice personalizzato per ogni pagina che
#presenta una struttura diversa dalle altre.
#Per questo partiamo dal 1987.
years= [x for x in range(1987,1988)] 
#print(years)

data= []


#creo i page name  delle pagine wikipedia che contengono i defunti
#di quel mese e di quell'anno e li inserisco in una lista.
#questo perchè tutte le pagine wikipedia dal 1987 in poi si chiamano:
#Deaths_in_mese_anno.
#Esempio: Deaths_in_may_1995

page_name= []
page_false= []

for anno in years:
    for mese in months:
        stringa= "Deaths_in_"
        stringa= stringa + mese + "_" + str(anno)
        page_name.append(stringa)
        #check_exists(wiki_wiki, stringa)

'''
for page in page_name:
    print(page)
'''

#print("\n")


# Ottenere il testo completo di una pagina Wikipedia
# Ciclo unna per volta, su ogni pagina wikipedia Deadth_ dal 1987 in poi 
for page_dead in page_name:
    #print(page_dead)
    page= wiki_wiki.page(page_dead)
    #print(page.text)

    #cont=1
    stringa= ""
    testo= []

    #compongo parola per parola del testo
    for p in page.text:
        if p != " " and p != "\n":
            stringa= stringa + p
        else:           
            testo.append(stringa)

            if p == "\n":
                testo.append(p)

            stringa= ""


    #print(testo)


    #compongo una frase dopo ogni a capo ("\n")
    stringa= ""
    parsificazione_testo= []

    for string in testo:
        #print(string)
        if string != "\n":
            stringa= stringa + " " + string
        elif string == "\n":
            parsificazione_testo.append(stringa)
            stringa= ""

    #print(parsificazione_testo)
    #print("\n")





    day= 1
    blocco= 0
    str_day= " " + str(day)
    stringa= ""
    name_dead= []
    dict= {}
    month_year= {}

    #creo una lista di dizionari (dict), dove ogni dizionario ha come chiave il giorno
    #e come valore tutte le persone defunte in quel giorno

    for x in parsificazione_testo:
        #print(type(str_cont),type(x))
        if str_day == x:   # individua il giorno
            #print(x)

            key= x
            name_dead= []

            day += 1
            str_day = " " + str(day)
            blocco= 1

        if blocco == 1: # trovato il giorno, se non lo è già, diventerà la chiave del dizionario "dict"
            if key not in dict:
                dict[key]= ""
            else:       # altrimenti, se lo è già, gli assegno come valore una lista contenente tutte le persone defunte in quel giorno. La stringa di ogni persona contiene: nome, età, cosa faceva quando era in vita e in alcuni casi la causa della morte.
                name_dead.append(x)
                dict[key]= name_dead    # alla chiave (giorno del mese) assegno la lista contenete la persona defunta che poi si aggiorna di volta in volta fino a contenere tutte le persone defunte in quel giorno (chiave).


    #print(name_dead)
    #assegno la lista di dizionari (dict) a un altro 
    #dizionario (moth_year) che ha come chiave il mese e l'anno
    #della pagina contenente i defunti venuti a mancare in
    #questo periodo, e come valore la lista di dizionari (dict)
    month_year[page_dead]= dict

    #il tutto è contenuto in una lista (data)
    data.append(month_year)

    '''
    for x in name_dead:
        print(x)
    '''

print("\n")
#creo il database in formato json
#.dumps() comando per convertire un elemento python in json
database= json.dumps(data)
#print(database)


#Stampo la lista (data) di dizionari (month_year )che ha come chiave: 
#il mese e l'anno della pagina contenente i defunti venuti a mancare
#in questo periodo, e come valore la lista di dizionari (dict) 
#contenete come chiave: il giorno e come valore: una lista (name_dead)
#delle persone defunte.

for x in data:
    for key, value in x.items():
        print(f"{key}\n")
        for k, v in value.items():
            print(f"{k}\n")
            for valore in v:
                print(f"{valore}\n")

    print("\n")








'''
#Genero tutti gli URL delle pagine wikipedia che contengono i defunti
#di quel mese e di quell'anno e li inserisco in una lista.
URL= "https://en.wikipedia.org/wiki/Deaths_"

URLS= []

for anno in years:
    for mese in months:
        URLS.append(URL + "in" + "_" + mese + "_" + str(anno))

for url in URLS:
    print(url)
'''


