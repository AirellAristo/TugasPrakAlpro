#Latihan 2.3 

gajiPerjam = int(input("Masukkan Gaji Perjam Yang Anda Inginkan : "))
jamKerja = int(input("Masukkan Jumlah Jam kerja Yang Akan Dilakukan Dalam 1 Minggu : "))

#Soal1
totalGaji = gajiPerjam*(jamKerja*5)

#Soal2
setelahPajak =  totalGaji - (totalGaji*14/100)

#Soal3
membeliBaju = (setelahPajak*10/100)

#Soal4
membeliAlatTul = (setelahPajak*1/100)
sisaUang = setelahPajak - membeliBaju - membeliAlatTul

#Soal5
uangSedekah = (sisaUang*25/100)

#Soal6 
anakYatim = (uangSedekah*30/100)

#Soal7
anakDhuafa = uangSedekah-anakYatim

print("====== Hasil Perhitungan ======")
print("Pendapatan Budi Sebelum Melakukan Pembayaran Pajak Rp.",
      int(totalGaji))
print("Pendapatan Budi Setelah Melakukan Pembayaran Pajak Rp.",
      int(setelahPajak))
print("Jumlah Uang Yang Akan Dipakai Untuk Membeli Pakaian dan Aksesoris Rp.",
      int(membeliBaju))
print("Jumlah Uang Yang Akan Dipakai Untuk Membeli Alat Tulis Rp.",
      int(membeliAlatTul))
print("Jumlah Uang Yang Akan Disedekahkan Rp.",
      int(uangSedekah))
print("Jumlah Uang Yang Akan Diterima Anak Yatim Rp.",int
      (anakYatim))
print("Jumlah Uang Yang Akan Diterima Anak Dhuafa Rp.",int
      (anakDhuafa))