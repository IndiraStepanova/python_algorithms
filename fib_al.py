#1
def fib_1(n): 
    assert n >= 0
    return n if n <= 1 else fib_1(n-1) + fib_1(n-2)
#print(fib_1(8)) #много повторяющихся вычислений

#2 исключаем повторяющиеся вычисления путем использования словаря, но остается проблема с глобальной переменной
cache = {} 
def fib_2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib_2(n-1)+fib_2(n-2)
    return cache[n]
#print(fib_2(80)) 

#3 используем декоратор для создания локальной переменной cache, но затем запоминает результаты декорируемой функции в cache
def memo(f): 
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner #преимущество в том, что декоратор можно использвать с функцией, которая ничего про кэширование не знает, н-р,превратить fib_1 в fib_2
#fib_1 = memo(fib_1)
#print(fib_1(80))

#4 можно использовать lru_cache из стандартной библ python
from functools import lru_cache
fib_1 = lru_cache(maxsize=None)(fib_1)
print(fib_1(80))