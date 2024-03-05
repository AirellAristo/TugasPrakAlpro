#Latihan 4.2

def cek_digit_belakang(a,b,c) :
    toStringA = str(a)
    toStringB = str(b)
    toStringC = str(c)
    if (toStringA[len(toStringA)-1] == toStringB[len(toStringB)-1] 
        or toStringA[len(toStringA)-1] ==  toStringC[len(toStringC)-1] 
        or toStringB[len(toStringB)-1] ==  toStringC[len(toStringC)-1]) :
        return True 
    else :
        return False



print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))
