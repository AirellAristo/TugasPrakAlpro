#Latihan 7.2

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
cari = input("Kata Yang Mau Dihitung : ")


def hitungFrekuensi(kalimat,kata) : 
    lowerKalimat = kalimat.lower() 
    return lowerKalimat.count(kata.lower())

print(hitungFrekuensi(kalimat,cari))