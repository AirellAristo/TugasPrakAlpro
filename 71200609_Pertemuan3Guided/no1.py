#Latihan 3.1

try :
    suhu = int(input("Masukkan suhu tubuh: "))
    if suhu >= 38:
        print("Anda demam")
    else : 
        print("Anda Tidak Demam")
except : 
    print("Invalid Input")

#Latihan 3.2 

try :
    bilangan = int(input("Masukkan suatu bilangan: "))
except:
    print("Invalid Input")
else :
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")

#Latihan 3.3
# input a, b dan c
try :
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))
except :
    print("Invalid Input")
else :     
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)