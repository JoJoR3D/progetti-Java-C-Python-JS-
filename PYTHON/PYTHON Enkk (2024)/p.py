import csv

with open("C:/Users/Giuse/OneDrive/Desktop/PYTHON Enkk (2024)/mappa.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=";")
    header= next(lettore)
    print(header)