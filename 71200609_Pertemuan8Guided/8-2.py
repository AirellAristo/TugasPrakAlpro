#Latihan 8.2 

file = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan8\\71200609_Pertemuan8Guided\\latihan2.txt","r")

simpan = dict()
hitung = 0
for baris in file : 
    x = baris.split(" || ")
    simpan[hitung] = x
    hitung += 1

namaFile = file.name.split("\\")[-1]
print("Nama File :",namaFile)
file.close()

for i in range(len(simpan)) : 
    print(simpan[i][0])
    jawaban = str(input("Jawab : "))
    lowerJawaban = jawaban.lower()
    NWJawaban = lowerJawaban.replace(" ","")
    lowerCheck = simpan[i][1].lower()
    NECheck = lowerCheck.replace("\n","")
    NWCheck = NECheck.replace(" ","")
    if NWJawaban == NWCheck : 
        print("Jawaban Benar !")
    else : 
        print("Jawaban Salah !")

