#Latihan 10.1

Dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

def keyValue(dictionary) :
    print("Key      Value      Item") 
    for key in dictionary :
        print(key,"      ",dictionary[key],"       ",key)


keyValue(Dict)