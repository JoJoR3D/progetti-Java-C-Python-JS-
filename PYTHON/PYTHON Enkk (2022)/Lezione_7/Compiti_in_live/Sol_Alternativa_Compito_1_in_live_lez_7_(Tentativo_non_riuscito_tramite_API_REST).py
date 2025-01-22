import requests

'''
API endpoint per eseguire la richiesta è: https://en.wikipedia.org/w/api.php
seguito poi da vari parametri, ad esempio:

- action= che indica che tipo di azione vogliamo svolgere sulla pagina.
  Possiamo passagli il parametro 'parse' che può essere utilizzata 
  per recuperare il contenuto della pagina in formato HTML (analizzato) 
  o in formato Wikitext (non analizzato).

- page= a cui passiamo il titolo della pagina wikipedia che 
  vogliamo analizzare

- format= al formato di visualizzazione dei dati della pagina wikipedia

'''


def spazi(var):
    stringa= ""
    for i in range(len(var)):
        if var[i] == " ":
            stringa= stringa + "_"
        else:
            stringa= stringa + var[i]
    
    return stringa




response= requests.get("https://en.wikipedia.org/w/api.php?action=parse&prop=links&page=Lists_of_deaths_by_year&format=json").json()

#print(response.content)
cont= 0

for key,value in response.items():  
    if key == "parse":                  #parse è la chiave che contiene come valore una lista
        #print(value)
        for dict in (value["links"]):   #value["links"] è una lista che contiene vari dizionari
            #print(dict)
            if cont > 3:
                for k,v in dict.items():    #accedo al valore del dizionario value["links"] con chiave "links"
                    #print(k)
                
                    if k == "*":  #quando trovo la chiave "*" ne salvo il valore (v). Il valore sono link agli anni che contengono le persone defunte in quel anno
                        #print(v)
                        link= spazi(v)      # 'v' mi ritorna una stringa con spazi. Uso la function spazi per sostituire gli spazi con "_". Altrimenti la richiesta API non funzionerebbe
                        LINK= "https://en.wikipedia.org/w/api.php?action=parse&page=" + link + "&format=json"
                        print(link)
                        print(LINK)
                        r= requests.get(LINK).json()
                        print(r)
                        '''
                        for chiave,valore in r.items(): #accedo alla pagina del primo anno e ne voglio salavare i nomi delle persone defunte in quel anno
                            if chiave == "parse":
                                for dd in (valore["links"]):   #value["links"] è una lista che contiene vari dizionari
                                    print(dd) 
                        '''
            cont += 1

            if cont>4:
                break
                
        
