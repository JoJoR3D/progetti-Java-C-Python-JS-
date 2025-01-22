import time


def conto_rovescia(tempo):
    while int(tempo) > 0:
        time.sleep(1)       # rallente l'esecuzione del programma di 1 secondo
        tempo= int(tempo)-1
        print(tempo)

    print("ALLARME!!!!!")




# MAIN

tempo= input("Indicare il tempo del conto alla rovescia in secondi\n")

conto_rovescia(tempo)
