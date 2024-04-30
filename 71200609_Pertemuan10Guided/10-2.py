def minMaxList(x) : 
    print("Terbesar :",max(x))
    print("Terkecil :",min(x))

list = []

while (True) :
    user = input("Masukkan Angka :")
    if user ==  "done" : 
        minMaxList(list)
        break
    else : 
        list.append(user)