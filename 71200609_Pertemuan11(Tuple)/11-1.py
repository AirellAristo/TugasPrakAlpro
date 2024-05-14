#Latihan 11.1
tA = (90,90,90,90)

def allEqual(x) : 
    count = 0 
    simpan = x[0]
    for i in x : 
        if simpan == i : 
            count += 1
    if count == len(x) :
        return True 
    else : 
        return False 



print(allEqual(tA))