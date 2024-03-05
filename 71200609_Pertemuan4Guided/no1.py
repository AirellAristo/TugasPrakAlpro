#Latihan 4.1 

def cek_angka(a,b,c) : 
    if a != b and a != c and b!= c :
        if a+b == c or a+c == b or b+c == a :
            return True 
        else : 
            return False
    else : 
        return False




print(cek_angka(1,4,5))
print(cek_angka(1,1,5))
print(cek_angka(1,4,1))
print(cek_angka(2,3,7))
print(cek_angka(5,4,1))