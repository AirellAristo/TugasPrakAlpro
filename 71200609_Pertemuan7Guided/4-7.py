#Latihan 7.3

def lowlong(kalimat) :
    split = kalimat.split(" ")
    terpanjang = split[0]
    terpendek = split[0]
    for kata in split : 
        if len(kata) > len(terpanjang) :
            terpanjang = kata
        if len(kata) < len(terpendek) :
            terpendek = kata 
    print(terpanjang)
    print(terpendek)

kalimat = "red snakes and a black frog in the pool"
lowlong(kalimat)