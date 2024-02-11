#Bagian 1
hargaAwal = 650000*25
hargaTerbaru = 685000*25
keuntunganA = hargaTerbaru-hargaAwal
keuntunganPersenA = (keuntunganA/hargaAwal)*100

print("====== Bagian 1 ======")
print("Keuntungan Dalam Rp ",keuntunganA)
print("Keuntungan Dalam Rp ",round(keuntunganPersenA,2),"%") 

#Bagian 2
tambahan = 685000*15
hargaTerbaruB = 715000*40
keuntunganB = (hargaTerbaruB) - (tambahan+hargaAwal)
keuntunganPersenB = (keuntunganB/(hargaAwal+tambahan))*100

print("====== Bagian 2 ======")
print("Keuntungan Dalam Rp ",keuntunganB)
print("Keuntungan Dalam Rp ",round(keuntunganPersenB,2),"%") 