#Latihan 10.4
fileName = input("Masukkan Nama File : ")

artikel = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan10\\71200609_Pertemuan10(Dictionary)\\"+fileName,"r")
sender = {}
for baris in artikel : 

    x = baris.lower()
    y = x.split()
    if len(y) > 1 : 
        if y[0] == "author:" :
            x1 = y[1].split("@")
            if x1[1] not in sender.keys() : 
                sender[x1[1]] = 1
            else :
                sender[x1[1]] += 1

print(sender)

