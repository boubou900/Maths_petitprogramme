def nbpremier(num):
    if num>2 and num%2==0:
        return False
    for x in range(2, num // 2):
        if num%x==0:
            return False
    return True
def decomp(nb):
    print(nb,"en produit de facteurs premiers vaut")
    a=4
    liste=[]
    i=2
    while nbpremier(a)==False:
        while nbpremier(i)==False:
            i+=1
        if nb%i==0:
            liste.append(i)
            nb=nb//i
            if nbpremier(nb)==True:
                liste.append(nb)
                a=2
        else:
            i+=1
    return liste
#nbadecomp=input('quel nombre entier superieur ou egal a 2 voulez vous decomposer en produit de facteurs premiers?')
#print(decomp(int(nbadecomp)))
for i in range(2,100):
    print(decomp(i))