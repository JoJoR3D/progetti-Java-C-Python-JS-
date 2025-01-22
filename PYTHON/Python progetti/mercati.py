import yfinance as yf
import pandas as pd


# HO CALCOLATO IL DRAWDOWN GIORNALIERO, ORA CALCOLO QUELLO MENSILE



# FUNCTION

# FUNCTION CHE VERIFICA IN QUALCHE PARTE DEL MESE, DI OGNI TRIMESTRE, (inizio,metà,fine) SI HA IL PREZZO PIU' BASSO IN UN DETERMINTO PERIODO DI TEMPO (es: 6mo, 1y)
def PM(data, prezzo_min, mese_del_prezzo_min, giorno_del_prezzo_min, diz_primo_trimestre, diz_secondo_trimestre, diz_terzo_trimestre, diz_quarto_trimestre):
    print(f"Prezzo più basso del mese\nData= {data}, Importo= {prezzo_min}")

    if int(mese_del_prezzo_min) < 4:
        prezzo_basso_mensile(int(giorno_del_prezzo_min[0]), diz_primo_trimestre)
    elif int(mese_del_prezzo_min) >= 4 and int(mese_del_prezzo_min) < 7:
        prezzo_basso_mensile(int(giorno_del_prezzo_min[0]), diz_secondo_trimestre)
    elif int(mese_del_prezzo_min) >= 7 and int(mese_del_prezzo_min) < 10:
        prezzo_basso_mensile(int(giorno_del_prezzo_min[0]), diz_terzo_trimestre)
    elif int(mese_del_prezzo_min) >= 10 and int(mese_del_prezzo_min) < 13:
        prezzo_basso_mensile(int(giorno_del_prezzo_min[0]), diz_quarto_trimestre)



# FUNCTION CHE VERIFICA IN QUALCHE PARTE DEL MESE, DI OGNI TRIMESTRE, (inizio,metà,fine) SI HA IL PREZZO PIU' BASSO IN UN DETERMINTO PERIODO DI TEMPO (es: 6mo, 1y)
def prezzo_basso_mensile(giorno, diz):
    if giorno < 15:
        diz["inizio_mese"]= diz["inizio_mese"] + 1

    elif giorno >= 15 and giorno < 22:
        diz["meta_mese"]= diz["meta_mese"] + 1

    elif giorno >= 22:
        diz["fine_mese"]= diz["fine_mese"] + 1



# FUNCTION CHE CONFRONTA QUAL E' IL PREZZO PIU' BASSO SE QUELLO DI APERTURA O DI CHIUSURA DI UNA SESSIONE GIORNALIERA
def prezzo_apertura_chiusura_giornaliera(diz, apertura, chiusura):
    if apertura < chiusura:
        diz["apertura"]= diz["apertura"] + 1
    else:
        diz["chiusura"]= diz["chiusura"] + 1



# FUNCTION CHE CALCOLA IL PREZZO MEDIO DI OGNI MESE
def prezzo_medio_mesile(prezzo_mese, prezzo_medio):
    prezzo_medio= prezzo_medio + prezzo_mese

    return prezzo_medio 



# FUNCTION PER CONTROLLARE SE IL PREZZO MEDIO SI AVVICINA PIU' AI PREZZI DELLA PRIMA META' DEL MESE O DELLA SECONDA META'
def vicinanza_prezzo_medio(prezzo_medio, prezzo_medio_prima_meta, prezzo_medio_seconda_meta):
    if prezzo_medio > prezzo_medio_prima_meta:
        differenza_1= prezzo_medio - prezzo_medio_prima_meta
    else:
        differenza_1= prezzo_medio_prima_meta - prezzo_medio

    if prezzo_medio > prezzo_medio_seconda_meta:
        differenza_2= prezzo_medio - prezzo_medio_seconda_meta
    else:
        differenza_2= prezzo_medio_seconda_meta - prezzo_medio


    if differenza_1 > differenza_2:
        print(f"Prezzo medio di {prezzo_medio} è più vicino alla sconda metà del mese che ha un prezzo medio di {prezzo_medio_seconda_meta}\n")
    else:
        print(f"Prezzo medio di {prezzo_medio} è più vicino alla prima metà del mese che ha un prezzo medio di {prezzo_medio_prima_meta}\n")

    
    



# FUNCTION PER IL CALCOLO PERCENTUALE (SUL PREZZO DI CHIUSURA DI INIZIO E FINE PERIODO) PER VERIFICARE L'ANDAMENTO DEL TITOLO IN UN DETERMINATO PERIODO DI TEMPO
def percentuali_mensili_prezzo(lista):
    #print(f"Lista: {lista}")
    differenza= lista[1] - lista[0]
    percentuale= (differenza*100)/lista[0]

    return percentuale



# FUNCTION PER LA PULIZIA DELLA LISTA PERCENTUALI
def pulizia_lista(lista):
    for i in range(len(lista)-1,-1,-1):
        lista.pop(i)



# FUNCTION PER CALCOLO DRAWDOWN GIORNALIERO DEL MESE IN CORSO
def drawdown(prezzo_iniziale_periodo, prezzo_corrente_periodo, prezzo_min):
    
    if prezzo_iniziale_periodo > prezzo_corrente_periodo:
        prezzo= prezzo_corrente_periodo - prezzo_iniziale_periodo

        #print(f"Pr_iniz: {prezzo_iniziale_periodo}, Pr_corr: {prezzo_corrente_periodo}, Pr_min: {prezzo_min}, Pr: {prezzo}")

        if prezzo < 0:
            if prezzo < prezzo_min:
                prezzo_min= prezzo

    return prezzo_min














# MAIN

titolo= yf.Ticker("SWDA.MI")

#print(titolo.info)

periodo= "1y"

history= titolo.history(period= periodo)
#print(type(history)
print(history)

print("\n")


'''
Non esiste un metodo per richiedere pandas.DataFrame, pandas.Series direttamente in list, ottenere prima l’array NumPy ndarray con l’attributo values, 
quindi utilizzare il tolist() per utilizzare in list.
Se si desidera mantenere l’etichetta come dati di elenco, reimpostare l’indice con il metodo reset_index().
'''
lista = history.reset_index().values.tolist()

#print(lista)

prezzo_min= 500

ciclo= 0
flag= 0
mese_del_prezzo_min= 0

prezzo_medio= 0
cont_prezzi= 0
cont_prezzi_prima_parte= 0
cont_prezzi_seconda_parte= 0
prezzo_medio_prima_parte= 0
prezzo_medio_seconda_parte= 0

primo_prezzo_per_drawdown= 0
prezzo_min_drawdown= 0.0
flag_in_per_drawdown= 0

lista_percentuali_mensili_prezzo= []
percentuale_totale= 0

diz_primo_trimestre= {"inizio_mese": 0, "meta_mese": 0, "fine_mese": 0}
diz_secondo_trimestre= {"inizio_mese": 0, "meta_mese": 0, "fine_mese": 0}
diz_terzo_trimestre= {"inizio_mese": 0, "meta_mese": 0, "fine_mese": 0}
diz_quarto_trimestre= {"inizio_mese": 0, "meta_mese": 0, "fine_mese": 0}

diz_apertura_chiusura_giornaliera= {"apertura": 0, "chiusura": 0}


for l in lista:    
    
    flag_in= 1
    flag_in_per_prezzo_apertura_chiusura= 1
    flag_in_per_percentuale= 1


    for i in range(0,len(l)):
        
        #indice 0 è la ("date");
        #indice 1 è il prezzo di apertura della giornata ("open"):
        #indice 2 è il prezzo massimo della giornata ("high")
        #indice 3 è il prezzo minimo della giornata ("low")
        #indice 4 indica il prezzo di chiusura di giornata ("close")
        #indice 5 indica il volume di scambi della giornata ("volume")
        #indice 6 i dividendi ("dividends")
        #indice 7 se c'è uno split dello stock ("stock splits")
        #indice 8 indica il capital gains ("capital gains")

        #print(l[i])

        # Per calcolo drawdown giornaliero del mese in corso
        if flag_in_per_drawdown == 1:
            prezzo_min_drawdown= drawdown(primo_prezzo_per_drawdown, l[1], prezzo_min_drawdown)
            flag_in_per_drawdown= 0


        primo_prezzo_per_drawdown= l[1]


        # Calcolo percentuale (sul prezzo di chiusura di inizio e fine periodo) per verificare l'andamento del titolo in un determinato periodo di tempo
        if (ciclo == 0 or ciclo == len(lista)) and flag_in_per_percentuale == 1:
            lista_percentuali_mensili_prezzo.append(l[4])
            if len(lista_percentuali_mensili_prezzo) == 2:
                percentuale= percentuali_mensili_prezzo(lista_percentuali_mensili_prezzo)
                pulizia_lista(lista_percentuali_mensili_prezzo)

                percentuale_totale= percentuale_totale + percentuale

            flag_in_per_percentuale= 0



        #RICAVO IL GIORNO PER SAPERE QUANDO ARRIVO AL 30 DEL MESE
        lista_data= str(l[0]).split("-")
        #print(lista_data[1], lista_data[2].strip("00:00:00+02:00"))      
                                
        giorno= lista_data[2].split(" ") #con .split() separo dal giorno la stringa contenente il fuso orario
        #print(giorno[0])        
             
        mese= lista_data[1]  

        #print(mese, mese_del_prezzo_min, int(giorno[0]), flag_in, flag)

        # Function che stampa la data e il prezzo ogni mese, per sapere se il prezzo minimo si è avuto a inizio, a metà o a fine mese.
        if mese != mese_del_prezzo_min and flag_in == 1 and flag == 1 and ciclo > 0:
            PM(data, prezzo_min, mese_del_prezzo_min, giorno_del_prezzo_min, diz_primo_trimestre, diz_secondo_trimestre, diz_terzo_trimestre, diz_quarto_trimestre)
            prezzo_min= 500
            flag_in == 0
            flag= 0

            PrezzoMedioMensile= prezzo_medio/cont_prezzi
            print(f"\nPrezzo medio mensile: {PrezzoMedioMensile}\n")
        
            # Per controllare se il prezzo medio si avvicina più ai prezzi della prima metà del mese o della seconda metà
            if cont_prezzi_prima_parte > 0 and cont_prezzi_seconda_parte > 0:
                PrezzoMedioPrimaParte= prezzo_medio_prima_parte / cont_prezzi_prima_parte
                PrezzoMedioSecondaParte= prezzo_medio_seconda_parte / cont_prezzi_seconda_parte
                vicinanza_prezzo_medio(PrezzoMedioMensile, PrezzoMedioPrimaParte, PrezzoMedioSecondaParte)

            print(f"Massimo drawdown giornaliero del mese: {prezzo_min_drawdown}\n\n\n")

            prezzo_medio= 0
            cont_prezzi= 0
            cont_prezzi_prima_parte= 0
            cont_prezzi_seconda_parte= 0
            prezzo_medio_prima_parte= 0
            prezzo_medio_seconda_parte= 0
            prezzo_min_drawdown= 0



        # Function che confronta qual e' il prezzo più basso, se quello di apertura o di chusura di una sessione giornaliera  
        # l[1] prezzo apertura; l[4] prezzo chiusura 
        if flag_in_per_prezzo_apertura_chiusura == 1:
            prezzo_apertura_chiusura_giornaliera(diz_apertura_chiusura_giornaliera, l[1], l[4])
            flag_in_per_prezzo_apertura_chiusura= 0



        if i == 4:
            # Function che calcola il prezzo medio di ogni mese
            # l[i] con i == 4 indica il prezzo di chiusura
            cont_prezzi += 1
            prezzo_medio= prezzo_medio_mesile(l[i], prezzo_medio)


            # Per controllare se il prezzo medio si avvicina più ai prezzi della prima metà del mese o della seconda metà
            if int(giorno[0]) > 0 and int(giorno[0]) < 16:
                prezzo_medio_prima_parte= prezzo_medio_prima_parte + l[i] 
                cont_prezzi_prima_parte += 1
            else:
                prezzo_medio_seconda_parte= prezzo_medio_seconda_parte + l[i]
                cont_prezzi_seconda_parte += 1


            # l[i] contiene il prezzo del periodo
            if l[i] < prezzo_min:
                prezzo_min= l[i]

                #RICAVO IL GIORNO DEL MESE CON IL PREZZO PIU' BASSO
                data= l[0]
                ld= str(data).split("-")
                #print(lista_data[1], lista_data[2].strip("00:00:00+02:00")) 
                                             
                giorno_del_prezzo_min= ld[2].split(" ") #con .split() separo dal giorno la stringa contenente il fuso orario
                #print(giorno_del_prezzo_min[0])     

                #per individuare il trimestre
                mese_del_prezzo_min= ld[1]  

                flag= 1
    
    flag_in_per_drawdown= 1

    ciclo += 1
    


  
# Per stampare il prezzo più basso dell'ultimo mese da analizzare
# altrimenti non lo stampa poichè il mese è == al mese_del_prezzo_min poichè dopo non essendoci altri mesi da analizzare, mese non verrà incrementato,
# e rimarrà == al mese_del_prezzo_min.
# Lo stesso val per il prezzo medio e per il calcolo percentuale
PM(data, prezzo_min, mese_del_prezzo_min, giorno_del_prezzo_min, diz_primo_trimestre, diz_secondo_trimestre, diz_terzo_trimestre, diz_quarto_trimestre) 

PrezzoMedioMensile= prezzo_medio/cont_prezzi
print(f"\nPrezzo medio mensile: {PrezzoMedioMensile}\n\n")

# Calcolo percentuale (sul prezzo di chiusura di inizio e fine periodo) per verificare l'andamento del titolo in un determinato periodo di tempo
lista_percentuali_mensili_prezzo.append(l[4])
if len(lista_percentuali_mensili_prezzo) == 2:
    percentuale= percentuali_mensili_prezzo(lista_percentuali_mensili_prezzo)
    pulizia_lista(lista_percentuali_mensili_prezzo)

    percentuale_totale= percentuale_totale + percentuale   



# Andamento in percentuale del titolo nell'arco di tempo di periodo calcolato sul prezzo di chiusura di inizio e fine periodo
print(f"\nAndamento in percentuale del titolo nell'arco di tempo di {periodo} calcolato sul prezzo di chiusura di inizio e fine periodo: {percentuale_totale}\n")



# Andamento per Trimestri
print("\n\nVERIFICA IN QUALCHE PARTE DEL MESE, DI OGNI TRIMESTRE, (inizio,metà,fine) SI HA IL PREZZO PIU' BASSO IN UN DETERMINTO PERIODO DI TEMPO (es: 6mo, 1y)")
print(f"\nPrimo_trimestre: {diz_primo_trimestre}")
print(f"\nSecondo_trimestre: {diz_secondo_trimestre}")
print(f"\nTerzo_trimestre: {diz_terzo_trimestre}")
print(f"\nQuarto_trimestre: {diz_quarto_trimestre}")


print(f"\n\nNumero di volte in cui il prezzo giornaliero è stato più basso in apertura o chiusura di sessione giornaliera nell'arco di tempo di {periodo}\n{diz_apertura_chiusura_giornaliera}")

print("\n")
