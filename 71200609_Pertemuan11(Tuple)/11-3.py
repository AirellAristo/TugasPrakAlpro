#Latihan 11.3
fileName = input("Enter A Name File : " )

text = open("c:\\Users\\Airell\\Documents\\Tugas Kampus\\Semester 8\\Praktikum AlPro\\Pertemuan11\\71200609_Pertemuan11(Tuple)\\"+fileName,"r")
dict = {}

for baris in text :
    x = baris.split()
    if len(x) >= 1 : 
        if x[0] == "From" :
            jam = x[5].split(":")[0]
            if jam not in dict.keys() : 
                dict[jam] = 1
            else : 
                dict[jam] += 1

sorted_data = {key: dict[key] for key in sorted(dict.keys())}
for key,value in sorted_data.items() : 
    print(key, value)