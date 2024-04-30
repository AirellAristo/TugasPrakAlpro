artikel = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan9\\71200609_Pertemuan10Guided\\artikel.txt","r")

kataUnik = []

for baris in artikel : 
    NNBaris = baris.strip()
    splitBaris = NNBaris.split(" ")
    for kata in splitBaris : 
        if kata not in kataUnik : 
            kataUnik.append(kata) 
 
artikel.close()
print(kataUnik)