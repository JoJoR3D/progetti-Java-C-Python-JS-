#COMPITO 2 Lezione 03
#Scrivere una funzione main che testi un insieme di funzioni:
'''
• Una funzione re(list) che prenda in input una lista e ne restituisca 
una nuova con i valori invertiti

• Una funzione is_positive(n) che controlli se un numero è positivo 
oppure no (restituisce True o False), si faccia uso dell'operatore 
di resto %

• Una funzione che prende come parametro una lista e ne restituisca 
una nuova con gli stessi valori ma priva di duplicati 
(si preservi l'ordine degli elementi!)

• Una funzione che controlli se una stringa è palindroma oppure no 
(restituisce True o False)

• Una funzione che restituisca il fattoriale di un numero intero n dato 
come argomento. Si implementi questa soluzione usando un loop 
(e se non potessimo usare i loop? difficile: funzione ricorsiva)
'''

'''
Per testare si intende (qui il test e implementazione della funzione 
ipotetica somma):

def main():

x = 1

y = 3

if somma(x,y) == 4:

print("Funzione somma ok")

else: print("Funzione somma non ok")

def somma(x, y): return x+y
'''




#ESECUZIONE:
#• Una funzione re(list) che prenda in input una lista e ne restituisca 
#una nuova con i valori invertiti

list= []
relist= []

x= input("Inserire valori numerici o stringhe:\nPer interrompere l'inserimento digitare -1\n")

while x != '-1':
    list.append(x)
    x= input()

print(list)


n= len(list)

for i in range(n-1,-1,-1):
    relist.append(list[i])

print(f"Lista invertita: {relist}\n")




#• Una funzione is_positive(n) che controlli se un numero è positivo 
#oppure no (restituisce True o False), si faccia uso dell'operatore 
#di resto %

def is_positive(n):
    #resto= n%1
    if n >= 0:
        return True
    else:
        return False
    

#MAIN
numero= -5
print(is_positive(numero))






#• Una funzione che prende come parametro una lista e ne restituisca 
#una nuova con gli stessi valori ma priva di duplicati 
#(si preservi l'ordine degli elementi!)

def fun(list):
    new_list= []
    n= len(list)
    verifica= 0

    for i in range(n):
        if i > 0:
            for y in range(len(new_list)):
                if list[i] == new_list[y]:
                    verifica= 1
                    break;
            
            if verifica == 0:
                new_list.append(list[i])

        else:
            new_list.append(list[i])
        
        verifica= 0

    return new_list


#MAIN
lista= []
valore= input("\nInserire valori numerici o stringhe:\nPer interrompere l'inserimento digitare -1\n")

while valore != '-1':
    lista.append(valore)
    valore= input()

nuova_lista= fun(lista)
print(nuova_lista)






#• Una funzione che controlli se una stringa è palindroma oppure no 
#(restituisce True o False)

stringa= input("\nInserire una stringa:\n")
new_string= ""
n= len(stringa)

#copio la stringa invertita in un'altra stringa

for i in range(n-1,-1,-1):
    new_string= new_string + stringa[i]

#controllo per vedere se sono palindrome

if stringa == new_string:
    print("\nLa stringa è palindroma")
else:
    print("\nLa stringa non è palindroma")






#• Una funzione che restituisca il fattoriale di un numero intero n dato 
#come argomento. Si implementi questa soluzione usando un loop 
#(e se non potessimo usare i loop? difficile: funzione ricorsiva)

n= int(input("Inserire un numero intero positivo per calcolarne il fattoriale\n"))
fatt= 1

for i in range(1,n+1):
    fatt= fatt*i

print("\nCalcola fattoriale mediante ciclo for:", fatt)


#calcola fattoriale di 'n' mediante funzione ricorsiva

def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n*fattoriale(n-1)

print("\nCalcolo fattoriale mediante funzione ricorsiva:", fattoriale(n))



#per esercitarmi, funzione ricorsiva per la somma di 'm' numeri

m= 6

def somma(m):
    if m == 0:  #CASO BASE
        return 0
    else:
        return m+somma(m-1)
    
print(f"\nCalcolo somma dei primi {m} numeri naturali mediante funzione ricorsiva:", somma(m))

#SPIEGAZIONE:
#congelato nello stack le seguenti chiamate:

'''
m= 6

6 + somma(5)
5 + somma(4)
4 + somma(3)
3 + somma(2)
2 + somma(1)
1 + somma(0)

con somma(0) mi trovo nel caso base. m==0 mi ritrona 0 (risultato somma(0))
quindi rientro nello stack:

1 + 0= 1   risultato di somma(1)
2 + 1= 3   risultato di somma(2)
3 + 3= 6   risultato di somma(3)
4 + 6= 10  risultato di somma(4)
5 + 10= 15 risultato di somma(5)
6 + 15= 21 risultato di somma(6)

21 è il risultato della somma dei primi 6 numeri naturali.

'''