#Latihan 4.3

suhu= int(input("C = "))


konversi_suhu = [lambda suhu : "F = " + str(int((9/5) * suhu +32)),
                lambda suhu :"R = " +  str(int(0.8 * suhu))]
print("Input C =", suhu, "Output",konversi_suhu[0](suhu))
print("Input C =", suhu, "Output",konversi_suhu[1](suhu))