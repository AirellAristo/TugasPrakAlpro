#Latihan 7.1

def checkAnagram(kata,checkKata) :
    noSpaceKata = kata.replace(" ","")
    noSpaceCheckKata = checkKata.replace(" ","")
    hitung = 0
    if len(noSpaceKata) == len(noSpaceCheckKata) :
        for huruf in noSpaceCheckKata :
            if noSpaceCheckKata.count(huruf) == noSpaceKata.count(huruf) :
                hitung += 1
        if len(noSpaceKata) == hitung :
            print(checkKata,"anagram dengan",kata)
        else :
            print(checkKata,"bukan anagram dari",kata)
    else : 
        print(checkKata,"bukan anagram dari",kata)
    
checkAnagram("mata","atma")
checkAnagram("mata","maat")
checkAnagram("mata","taam")
checkAnagram("mata","tama")
