#Latihan 5.1

def perkalian(a,b) :
    hitung = 0 
    print(a,"x",b,"=",end=" ")
    for i in range (a) :
        hitung += b
        if i != a-1 :
            print(str(b),end=" + ")
        else :
            print(str(b),"=",hitung)

perkalian(6,5)
perkalian(7,10)