#Jawaban Dimulai Pada baris 36

n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

# input nama kategori dan aplikasi di dalamnya
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)

# siapkan list kosong untuk nama-nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

# masukkan dalam dictionary
    data_aplikasi[nama_kategori] = aplikasi

# tampilkan dictionary data_aplikasi
print(data_aplikasi)

daftar_aplikasi_list = []

# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)

# lakukan intersection ke semua set yang ada
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

#Latihan 12.1

count = {}
for values in daftar_aplikasi_list : 
    for app in values : 
        if app not in count : 
            count[app] = 1
        else : 
            count[app] += 1
satuKategori = [aplikasi for aplikasi,x in count.items() if x == 1]
print("Aplikasi Yang Muncul Pada 1 Kategori", satuKategori)

if n > 2 :
    count = {}
    for values in daftar_aplikasi_list : 
        for app in values : 
            if app not in count : 
                count[app] = 1
            else : 
                count[app] += 1
    duaKategori = [aplikasi for aplikasi,x in count.items() if x == 2]
    print("Aplikasi Yang Muncul Pada 2 Kategori", duaKategori)


