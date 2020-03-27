#Factorial Sum

from math import factorial
while True:
    try:
        n, m = input().split()
        n, m = int(n), int(m)
        soma = factorial(n) + factorial(m)
        print(soma)
    except EOFError:
        break