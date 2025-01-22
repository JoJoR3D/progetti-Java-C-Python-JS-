from cryptography.fernet import Fernet

key= Fernet.generate_key()
f= Fernet(key)
print("Meddaggio cifrato:")
token= f.encrypt(b"Faccio la cacca tutti i giorni! Messaggio segreto!")

print(token)

print(f"\nMessaggio decifrato:\n{f.decrypt(token)}")

