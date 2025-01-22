import random as Random


alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabeto_maiuscolo= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caratteri_speciali= ['£','$','%','&','?']
numeri= [0,1,2,3,4,5,6,7,8,9]


Input= input("Si desidera generare una password? 1 per SI, 0 per NO\n")

    
if int(Input) == 1:

    in_char_minuscolo= 0
    in_char_maiuscolo= 0
    in_caratteri_speciali= 0
    in_numeri= 0

    # questo while controlla che almeno una volta venga generato uno di tutto (caratteri maiuscoli e minuscoli, caratteri speciali e numeri)
    # se così non fosse, allora si resetta tutto e si ripete a generare una nuova password
    while in_char_maiuscolo == 0 or in_char_minuscolo == 0 or in_caratteri_speciali == 0 or in_numeri == 0:
        i= 0
        cont_char= 0
        cont_num= 0
        password= ""

        in_char_minuscolo= 0
        in_char_maiuscolo= 0
        in_caratteri_speciali= 0
        in_numeri= 0

        while i < 10:
            choice= Random.randint(0,2) # scegli se generare casualmente un carattere dell'alfabeto, un carattere speciale o un numero
            if choice == 0:
                choice_min_mai= Random.randint(0,1) # scegli se genersre casualmente un carattere dell'alfabeto minuscolo o maiuscolo
                if choice_min_mai == 0:
                    casual= Random.randint(0,len(alfabeto)-1)
                    password= password + alfabeto[casual]
                    in_char_minuscolo= 1
                else:
                    casual= Random.randint(0,len(alfabeto_maiuscolo)-1)
                    password= password + alfabeto_maiuscolo[casual]
                    in_char_maiuscolo= 1
        
            elif choice == 1 and cont_char < 3:  # si possono inserire al massimo 3 caratteri speciali (per evitare che venga generata una password che contenga troppi o solo caratteri speciali)
                casual= Random.randint(0,len(caratteri_speciali)-1)
                password= password + caratteri_speciali[casual]
                cont_char += 1
                in_caratteri_speciali= 1

            elif choice == 2 and cont_num < 3:  # come nel caso dei caratteri speciali, si possono inserire al massimo 3 numeri
                casual= Random.randint(0,len(numeri)-1)
                password= password + str(numeri[casual])
                cont_num += 1
                in_numeri= 1


            # se si è già superato il numero massimo di caratteri speciali o numeri inseribili e viene generato choice == 1 o choice == 2, la variabile 'i' non viene incrementata. In questo modo si avrà sempre una password di 10 caratteri.
            if (choice == 1 and cont_char >= 3) or (choice == 2 and cont_num >= 3):   
                i= i
            else:
                i= i+1

            #print(in_char_maiuscolo,in_char_minuscolo,in_caratteri_speciali,in_numeri)

    print("Password generata:", password)

else:
    print("OK!")
        