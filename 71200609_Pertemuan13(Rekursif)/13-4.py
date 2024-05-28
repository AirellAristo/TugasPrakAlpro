#Latihan 13.4

def sumDigit(n) :
    if len(n) == 0 : 
        return 0
    else : 
        if n.isnumeric() : 
            return int(n[0]) + sumDigit(n[1:])
        else : 
            return False
    
print(sumDigit("234"))
print(sumDigit("1a23"))