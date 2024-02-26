#Latihan 3.3
try :
    bulan = int(input("Masukkan Bulan (1-12) : "))
    jumlahHari = 0
    check = 1 


    if bulan == 1 : 
        jumlahHari += 31 
    elif bulan == 2 : 
        jumlahHari += 29 
    elif bulan == 3 : 
        jumlahHari += 31
    elif bulan == 4 : 
        jumlahHari += 30
    elif bulan == 5 : 
        jumlahHari += 31
    elif bulan == 6 : 
        jumlahHari += 30
    elif bulan == 7 : 
        jumlahHari += 31
    elif bulan == 8 : 
        jumlahHari += 31
    elif bulan == 9 : 
        jumlahHari += 30
    elif bulan == 10 : 
        jumlahHari += 31
    elif bulan == 11 : 
        jumlahHari += 30
    elif bulan == 12 : 
        jumlahHari += 31
    else : 
        check = 0 


    if check != 0 : 
        print("Jumlah Hari :",jumlahHari)
    else : 
        print("Masukkan Bulan Dari Range 1-12 saja")

except : 
    print("Invalid Input")