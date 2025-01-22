import wikipediaapi
import json

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI)

#page_py = wiki_wiki.page("Deaths_in_May_1989")
#print(page_py.text)



# FUNCTION

def check_exists(wiki_wiki, stringa):
    page_py = wiki_wiki.page(stringa)
    print(stringa, page_py.exists())

    #con .exists() controllo se le pagine web presenti in page_name
    #esistono oppure no
    if page_py.exists() == "False":
        page_false.append(stringa)


# Poichè quando stampo il database, in caso di doppia età: 56-57, il json non riconosce il "–" e mette caratteri diversi dopo il "–",
# quando trovo una doppia età, cambio il "–" con "/"
def sostituzione_eta(string):
    s= ""
    for x in string:
        if x == "–":
            s= s + "/" 
        else:
            s= s + x
    
    return s



# Poichè quando stampo il database, il json non riconosce i caratter indicati in list_char,
# li sostituisco con gli equivalenti senza apostrofi, accenti, ecc...
def sostituzione_nome(string):
    s= ""
    list_char= ["É", "è", "é", "ç", "ò", "ö", "à", "ù", "ü", "ì", "–"]

    for x in string:
        flag= 0
        for y in list_char:
            if x == y:
                if y == "è" or y == "é":
                    s= s + "e"
                    flag= 1

                elif y == "É":
                    s = s + "E"
                    flag= 1
                
                elif y == "ç":
                    s= s + "c"
                    flag= 1

                elif y == "ò" or y == "ö":
                    s= s + "o"
                    flag= 1

                elif y == "à":
                    s= s + "a"
                    flag= 1

                elif y == "ù" or y == "ü":
                    s= s + "u"
                    flag= 1

                elif y == "ì":
                    s= s + "i"
                    flag= 1

                elif y == "–":
                    s= s + "/"
                    flag= 1

        if flag == 0:
            s= s + x

    return s







# MAIN

months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#dal 1987 in poi le strutture delle pagini sono uguali. 
#Prima del 1987 hanno quasi tutte una struttura diversa. 
#Quindi ci vorrebbe un codice personalizzato per ogni pagina che
#presenta una struttura diversa dalle altre.
#Per questo partiamo dal 1987.
years= [x for x in range(1987,1988)] 
#print(years)




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



data= []

# Ottenere il testo completo di una pagina Wikipedia
# Ciclo una per volta, su ogni pagina wikipedia Deadth_ dal 1987 in poi 
for page_dead in page_name:
    #print(page_dead)
    page= wiki_wiki.page(page_dead)
    #print(page.text)


    
    parsificazione_testo= []

    #ricavo una stringa dal testo ad ogni a capo (.split("\n")) e le inserisco in una lista
    for p in page.text.split("\n"):
        parsificazione_testo.append(p)

    #print(testo)



    day= 1
    blocco= 0
    str_day= str(day)
    stringa= ""
    name_dead= []
    dict= {}
    month_year= {}

    #creo una lista di dizionari (dict), dove ogni dizionario ha come chiave il giorno
    #e come valore tutte le persone defunte in quel giorno

    for x in parsificazione_testo:
        #print(type(str_cont),type(x))
        #print(f"x: {x}\n")
        if x == str_day or x == "Unknown date":   # individua il giorno, se il giorno non c'è, nella pagina wikipedia vi è la stringa "Unknown date" dopo l'ultimo giorno del mese.
            #print(x)
            
            key= x
            name_dead= []

            day += 1
            str_day = str(day)
            blocco= 1
    
        if x == "== References ==" or x == "":
            blocco= 0

        if blocco == 1: # trovato il giorno, se non lo è già, diventerà la chiave del dizionario "dict"
            struttura_dict= {}
            
            if key not in dict:
                dict[key]= ""
            else:       # altrimenti, se lo è già, gli assegno come valore una lista contenente tutte le persone defunte in quel giorno. La stringa di ogni persona contiene: nome, età, cosa faceva quando era in vita e in alcuni casi la causa della morte.
                split= []
                split= x.split(",")                 #scompone una stringa ad ogni virgola, e ogni pezzo lo inserisce in una lista
                #print(f"x: {x}, LEN: {len(split)}")

                if len(split) > 2:                          # più di 2 elementi
                    split[0]= sostituzione_nome(split[0])
                    struttura_dict["name"]= split[0]
                    split[1]= sostituzione_eta(split[1].strip())    #.strip() elimina eventuali spazi
                    struttura_dict["age"]= split[1]
                    split[2]= sostituzione_nome(split[2])
                    struttura_dict["other"]= split[2]
                
                elif len(split) > 1 and len(split) <= 2:    # solo 2 elementi (ad esempio: "name" e "other")    
                    split[0]= sostituzione_nome(split[0])
                    struttura_dict["name"]= split[0]
                    # nel caso in cui non ci sia l'età ma solo il "name" e "other", raccolgo l'eccezione ValueError e assegno split[1] alla chiave: "other".
                    try:
                        if int(split[1]) == int:
                            split[1]= sostituzione_eta(split[1].strip())
                            struttura_dict["age"]= split[1]
                    except ValueError as Error:
                        #print(Error)
                        split[1]= sostituzione_nome(split[1])
                        struttura_dict["other"]= split[1]
                
                elif len(split) == 1:                       # solo 1 elemento (ad esempio solo "other")
                    if len(split[0]) <= 25:                 # può essere il "name"
                        split[0]= sostituzione_nome(split[0])
                        struttura_dict["name"]= split[0]
                    elif len(split[0]) > 25:                # è probabile che sia "other" poichè è difficile avere un nome con più di 25 caratteri
                        split[0]= sostituzione_nome(split[0])
                        struttura_dict["other"]= split[0]

                #print(struttura_dict)
                
                name_dead.append(struttura_dict)    #alla lista assegno il dizionario che ha come chiavi: "name", "age" e "other" (in alcuni casi, alcune di queste chiavi possono non comparire)
                dict[key]= name_dead    # alla chiave (giorno del mese) assegno la lista contenete la persona defunta che poi si aggiorna di volta in volta fino a contenere tutte le persone defunte in quel giorno (chiave).


    #print(name_dead)
    
    #assegno la lista di dizionari (dict) a un altro 
    #dizionario (moth_year) che ha come chiave il mese e l'anno
    #della pagina contenente i defunti venuti a mancare in
    #questo periodo, e come valore la lista di dizionari (dict)
    month_year[page_dead]= dict

    #il tutto è contenuto in una lista (data)
    data.append(month_year)




print("\n")
#creo il database in formato json
#.dumps() comando per convertire un elemento python in json
database= json.dumps(data)      #indent è un parametro di json.dumps()
#print(database)


#Stampo la lista (data) di dizionari (month_year )che ha come chiave: 
#il mese e l'anno della pagina contenente i defunti venuti a mancare
#in questo periodo, e come valore la lista di dizionari (dict) 
#contenete come chiave: il giorno e come valore: una lista (name_dead)
#che contiene i dizionari che hanno come chiavi: "name", "age" e "other" 
#(in alcuni casi, alcune di queste chiavi possono non comparire)
#delle persone defunte.

for x in data:
    for key, value in x.items():
        print(f"{key}\n")
        for k, v in value.items():
            print(f"{k}\n")
            for valore in v:
                print(f"{valore}\n")

    print("\n")
