#Latihan 5.2

def deretBilanganGanjil(bawah,atas):
    if bawah < atas :
        for i in range(bawah,atas+1): 
            if i % 2 != 0 :
                print(i,end="." if atas-1 == i or atas == i else ", ")
    else : 
        for i in range(bawah,atas-1,-1): 
            if i % 2 != 0 :
                print(i,end="." if atas+1 == i or atas == i else ", ")


# deretBilanganGanjil(10,30)
# deretBilanganGanjil(97,82)