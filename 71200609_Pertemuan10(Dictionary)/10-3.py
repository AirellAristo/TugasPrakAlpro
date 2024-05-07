#Latihan 10.3
fileName = input("Masukkan Nama File : ")

artikel = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan10\\71200609_Pertemuan10(Dictionary)\\"+fileName,"r")
sender = {}
for baris in artikel : 

    x = baris.lower()
    y = x.split()
    if len(y) > 1 : 
        if y[0] == "author:" :
            if y[1] not in sender.keys() : 
                sender[y[1]] = 1
            else :
                sender[y[1]] += 1

print(sender)

