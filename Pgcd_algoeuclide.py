def pgcd(a,b):
    fin=False
    if a<b :
        plus_grand=b
        plus_petit=a
    else:
        plus_grand=a
        plus_petit=b
    while fin!=True:
        reste=plus_grand%plus_petit
        if reste==0:
            fin=True
        plus_grand=plus_petit
        plus_petit=reste
    return plus_grand
a=int(input('nbr 1?'))
b=int(input('nbr 2?'))
print(pgcd(a,b))
