#1 вычислить число фибоначи
def fib(n):
    f1 = 1
    f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return f2
    

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

#2 необходимо найти последнюю цифру nn-го числа Фибоначчи
def fib(n):
    f1 = 1
    f2 = 1
    for i in range(2, n):
        f1, f2 = f2%10, (f1 + f2)%10
    return f2
    

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()