#Latihan 11.2
Data= ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

def dataDiri(x) :
    print("NIM :",x[1])
    print("NAMA :",x[0])
    print("ALAMAT :",x[2])
    print()
    nama = x[0].split()
    namaTerbalik = [nama[len(nama)-1-i] for i in range(len(nama))]
    print("NIM :",tuple(x[1]))
    print("NAMA DEPAN :",tuple(nama[0]))
    print('NAMA TERBALIK :', tuple(namaTerbalik))

dataDiri(Data)