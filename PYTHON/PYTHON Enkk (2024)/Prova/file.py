frase= "Cavolo nero"

file= open("doc.txt", "w")

file.write(frase)

file.close()





file= open("doc.txt", "a")

file.write("\nCavolo bianco è meglio")

file.close()




file= open("doc.txt", "r").readlines()

print(file)




file= open("doc.txt", "r")

riga= file.readline()

while riga != "" :
   print(riga)
   riga= file.readline()

file.close() 






import os

os.getcwd()

os.chdir("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2024)")

frase= "corro!"

file= open("doc.txt", "w")

file.write(frase)

file.close()