#Latihan 6.2

inputUser = int(input("n = "))

def deretBilangan(n) :
    hitung = 1
    for i in range (n) :
        for j in range(n,0,-1):
            hitung *= j 
        print(hitung, end=" ")
        for k in range(n,0,-1):
            print(k, end=" ")
        hitung = 1
        n -= 1
        print()

deretBilangan(inputUser) 