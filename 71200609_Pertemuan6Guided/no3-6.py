#Latihan 6.3

tinggi = int(input("Tinggi = "))
lebar = int(input("Lebar = "))

def deretBilangan(tinggi,lebar) : 
    deret = 1
    for i in range (tinggi) : 
        for j in range (lebar) :
            print(deret,end=" ")
            deret += 1
        print()
    

deretBilangan(tinggi,lebar)