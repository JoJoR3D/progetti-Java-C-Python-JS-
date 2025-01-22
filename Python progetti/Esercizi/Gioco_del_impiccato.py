
'''
Gioco dell'impiccato:
Un giocatore pensa ad una parola e l'altro deve indovinarla.
Chi deve indovinare, ad ogni lettera che non fa parte della parola scelta dal altro giocatore, si incrementa il contatore degli errori.
Si possono commettere al massimo 5 errori, al 6 il gioco termina.
'''


# FUNCTION

# controlla che la lettare inserita dal player_2 sia o presente nella parola da indovinare (return 2), se è stata già inserita (return 1), oppure nessuna delle due (return 0).

def check_lettera(list, lettera, parola_player_1):
    if lettera in list:
        return 1
    elif lettera not in parola_player_1:
        return 2
    else:
        return 0
        


# costruisce la parola che il player_2 sta componendo e la mostra. AL posto delle lettere ancora da indovinare viene mostrato '*' 

def costruzione_parola(p_player_1, l_player_2, word):
    parola= ""
    for i in range(0,len(p_player_1)):
        if l_player_2 == p_player_1[i]:
            parola= parola + l_player_2
        elif word[i] != '*':
            parola= parola + word[i]
        else:
            parola= parola + '*'

    word= parola

    return word



# controlla se il player_2 ha indovinato tutte le lettere della parola inserita dal player_2

def check_win(parola_player_1, parola_player_2):
    if parola_player_2 == parola_player_1:
        return 1 







# MAIN

cont_errori= 0
list_lettere= []
parola= ""


parola_player_1= input("Player 1, inserisca la parola:\n")
len_parola_player_1= len(parola_player_1)


print(f"Player 2, la parola da indovinare è lunga {len_parola_player_1}")

# assegna alla parola che il player_2 deve comporre tutti '*'
for i in range(0,len_parola_player_1):
    parola= parola + '*'




while cont_errori < 5:
    lettera_player_2= input("\nInserisca lettera: ")

    check= check_lettera(list_lettere, lettera_player_2, parola_player_1)
    print(check)

    if check == 1:
        print("La lettera inserita è stata già usata in precedenza")
    
    elif check == 2:
        print("Errore! La lettera non fa parte della parola da indovinare")
        list_lettere.append(lettera_player_2)
        cont_errori += 1
        print(f"Si hanno ancora {5-cont_errori} tentativi")

        if cont_errori == 5:
            print("\nHAI PERSO!")
    
    else:
        parola= costruzione_parola(parola_player_1, lettera_player_2, parola)
        list_lettere.append(lettera_player_2)
        print(parola)
        win= check_win(parola_player_1, parola)

        if win == 1:
            print("\nHAI VINTO! Hai indovinato la parola")
            break

