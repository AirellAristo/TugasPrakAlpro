#Latihan 12.2

dataList = ["apple","banana","cherry","apple"]
dataTuple = ("apple","banana","cherry","apple")

listToSet = set(dataList)
print("data sebelum konversi (List -> Set) = ",dataList)
print("data sesudah konversi (List -> Set) = ",listToSet)
print("")

setToList = list(listToSet)
print("data sebelum konversi (Set -> List) = ",listToSet)
print("data sesudah konversi (Set -> List) = ",setToList)
print("")

tupleToSet = set(dataTuple)
print("data sebelum konversi (Tuple -> Set) = ",dataTuple)
print("data sesudah konversi (Tuple -> Set) = ",tupleToSet)
print("")

setToTuple = tuple(tupleToSet)
print("data sebelum konversi (Set -> Tuple) = ",tupleToSet)
print("data sesudah konversi (Set -> Tuple) = ",setToTuple)
print("")