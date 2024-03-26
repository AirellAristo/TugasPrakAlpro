#Latihan 7.3

def spasiBerlebih(kalimat) :
    x = kalimat.lower()
    x1 = kalimat.split(" ")
    hitung = 0
    print('"',end="")
    for kata in x1 : 
        if kata != "" : 
            hitung += 1
            print(kata,end=" " if hitung != len(x1) - x1.count("") else '"')

kalimat = "saya    tidak suka memancing ikan "
spasiBerlebih(kalimat)