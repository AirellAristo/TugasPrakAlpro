#Latihan 10.2

Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

def combList(a,b) : 
    dict = {}
    for i in range(len(a)) : 
        dict[a[i]] = b[i]
    return dict

print(combList(Lista,Listb))