#Latihan 3.4
try :
    sisi1 = int(input("Masukkan Sisi 1 : "))
    sisi2 = int(input("Masukkan Sisi 2 : "))
    sisi3 = int(input("Masukkan Sisi 3 : "))
    
# 1 1 1
    if sisi1 == sisi2 and sisi1 == sisi3 :
        print("3 sisi sama")
    elif sisi1 == sisi2 and sisi1 != sisi3 : 
        print("2 sisi sama")
    elif sisi1 == sisi3 and sisi1 != sisi2 :
        print("2 sisi sama") 
    elif sisi2 == sisi3 and sisi2 != sisi1 : 
        print("2 sisi sama")
    else : 
        print("Tidak ada sisi yang sama")
except : 
    print("Inputan tidak valid ")