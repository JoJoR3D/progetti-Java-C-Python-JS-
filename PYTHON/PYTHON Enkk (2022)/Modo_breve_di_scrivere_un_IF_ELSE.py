a1_album= 2
a2_album= 3

solution= 0

if a1_album > a2_album:
    solution= 1
else:
    solution= 2

#Modo breve di scrivere l'if di sopra
sol= print(1) if a1_album > a2_album else print(2) 

#Altra soluzione
risultato= print("Corretto") if a1_album > a2_album else print("Sbagliato")