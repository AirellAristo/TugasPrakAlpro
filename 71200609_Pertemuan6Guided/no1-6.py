#Latihan 6.1 

def bilPrimaTerdekat(batas):
    angka = 2
    if batas <= 2 : 
        return "Tidak Ada Bilangan Prima Dibawah 2"
    if batas == 3 : 
        return angka 
    else :
        for i in range(batas):
            if i % 2 != 0:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    angka=i
        return angka
    
print(bilPrimaTerdekat(2))
print(bilPrimaTerdekat(3))
print(bilPrimaTerdekat(12))
print(bilPrimaTerdekat(21))
