file= open("documento.txt", "r").read()

print(file)







file= open("documento.txt", "a")

file.write("\nIo non ho paura!")

file.close()







file= open("documento.txt", "r").read()

print(file)






file= open("documento.txt", "r")

riga= file.readline()

while riga!= "":
   print(riga)
   riga= file.readline()

file.close()