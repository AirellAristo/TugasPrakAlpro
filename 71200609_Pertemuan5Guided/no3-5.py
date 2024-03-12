#Latihan 5.3

konversiNilai = {"A" : 12, "B" : 9, "C" : 6, "D" : 3}
totalNilai = 0 

print("Program Penghitung IPS Mahasiswa")
totalMatkul = int(input("Berapa Jumlah Mata Kuliah ? "))

for i in range(totalMatkul) :
    print("Nilai MK",i+1,end=": ")
    nilai = str(input())
    totalNilai += konversiNilai[nilai.upper()]

print("Nilai IPS Anda Semester Ini",round(totalNilai/(totalMatkul*3),2))