#COMPITO lezione 1andr

#Creare uno script di python che simuli il login ad un sito di casinò
#Si chieda all'utente nome cognome ed età. Si verifichi che il nome e il cognome sia più lungo di un carattere e che l'età sia maggiore o uguale a 18 anni.
#Se tutto è corretto stampare una stringa di conferma altrimenti comunicare l'errore all'utente.
#Si consideri che l'utente fornià sempre dati di tipo corretti.

#Stampare il resocondo dei dati assicurandoci che l'utente abbia inserito nome e cognome che cominciano con la maiuscola. 



#ESECUZIONE:
#Creare uno script di python che simuli il login ad un sito di casinò
#Si chieda all'utente nome cognome ed età. Si verifichi che il nome e il cognome sia più lungo di un carattere e che l'età sia maggiore o uguale a 18 anni.
#Se tutto è corretto stampare una stringa di conferma altrimenti comunicare l'errore all'utente.

print("---Login casino---\n")
nome= input("Inserire il proprio nome:\n")
cognome= input("Inserire il proprio cognome:\n")
eta= input("Inserire la propria età:\n")

if len(nome) > 1 and len(cognome) > 1 and int(eta) >= 18:
    print("\nAccesso consentito!")
    #Print a string of confirm if first letter of name and surname is uppercase
    if nome[0] == nome[0].capitalize() and cognome[0] == cognome[0].capitalize():
        print(f"\nNome: {nome.capitalize()}\nCognome: {cognome.capitalize()}\nEtà: {eta}")
else:
    print("\nAccesso negato!")
