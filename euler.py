#!/usr/bin/env python3

def euler1(n):
    return sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0])


# euler1(1000)


def fib(n):
    if (n > 3):
        fib = [1, 1]
        i = 0
        for i in range(n - 2):
            fib.append(fib[i] + fib[i+1])
        return fib
    else:
        if n > 0:
            return 1
        else:
            print('chose an integer value')


def euler2(n):
    fib = [1, 2]
    i = 0
    while fib[-1] < n:
        fib.append(fib[i] + fib[i+1])
        i += 1
    return sum([x for x in fib if x % 2 == 0])


# print(euler2(4000000))


def isprime(n):
    hasfactor = False
    i = 2
    from math import sqrt
    while not hasfactor and i < int(sqrt(n)):
        hasfactor = n % i == 0
        i += 1
    return not hasfactor


def euler3(n):
    lastfact = 1
    from math import sqrt
    for i in range(3, int(sqrt(n))):
        if n % i == 0 and isprime(i):
            lastfact = i
    return lastfact


print(euler3(600851475143))

def euler4():
    pass
