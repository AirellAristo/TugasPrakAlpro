#Latihan 13.3

def sumGanjil (n) :
    if n == 0 : 
        return 0
    if n % 2 != 0 :
        return n + sumGanjil(n -1)
    else : 
        return sumGanjil(n-1)


print(sumGanjil(10))