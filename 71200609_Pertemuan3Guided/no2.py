#Latihan 3.2
bilangan = int(input("Masukkan Sebuah Bilangan: "))
cek = (
    "Positif" if bilangan >= 1 else 
    ("Nol" if bilangan == 0 else 
    ("Negatif" if bilangan < 1  else "Invalid Input")))

print(cek)