teks1 = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan8\\71200609_Pertemuan8Guided\\latihan1a.txt","r")
teks2 = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan8\\71200609_Pertemuan8Guided\\latihan1b.txt","r")

teksA = []
teksB = []

for baris in teks1 : 
    x = baris.strip()
    teksA.append(x)

for baris in teks2 : 
    x = baris.strip()
    teksB.append(x)

for i in range(len(teksA)) : 
    if teksA[i] != teksB[i] : 
        print(teksA[i]," --- Tidak Sama dengan ---",teksB[i])

teks1.close()
teks2.close()

