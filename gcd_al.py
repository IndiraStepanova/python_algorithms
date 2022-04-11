import random

def test(gcd, n_iter=100): 
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(0, b) == b
        assert gcd(a, 1) == gcd(1, b) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0

#наивный алгоритм
def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b)+1)):
        if d == 0 or a % d == b % d == 0:
            return d
    
#test(gcd1)

#алгоритм евклида
def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b) #вернуть то число, которое не равно 0

#test(gcd2)

#рекурсивная версия алгоритма gcd2
def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

#test(gcd3)

#рекурсивная версия с явным чередованием
def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)


