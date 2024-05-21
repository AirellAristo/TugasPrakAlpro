#Latihan 12.3

kata = set()
for i in range(2): 
    fileName = input("Masukkan Nama File : ")
    try :
        text = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan12\\71200609_Pertemuan12(Set)\\"+fileName+".txt","r")
        for baris in text : 
            lower = baris.lower()
            kataSplit = lower.split()       
            if len(kataSplit) > 1 : 
                for i in kataSplit : 
                    kata.add(i)
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        break

if len(kata) > 0 : 
    print(kata)
