def pgcd(a,b):
    if a < b:
        a, b = b, a
    i=(a%b)
    while a != i:
        i = (a % b)
        if i == 0 :
            return b
        a, b = b, i

def bezout(a, b):
    pass
