#Latihan 13.2

def cekPalindrom (kata) : 
    kata1 = kata.replace(" ","")
    if len(kata1) == 0 :
        return True
    else : 
        if kata1[0] == kata1[-1] : 
            return cekPalindrom(kata1[1:len(kata1)-1])
        else :
            return False
        

print(cekPalindrom("rotator"))
print(cekPalindrom("makanan"))