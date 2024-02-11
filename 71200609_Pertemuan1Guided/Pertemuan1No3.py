danaAwal = 200
target = 400
tahun = 0 

bunga = 10/100

while True :
    if danaAwal >= target : 
        break
    else : 
        danaAwal += danaAwal * bunga
        tahun += 1

print("Waktu yang dibutuhkan",tahun,"Tahun")