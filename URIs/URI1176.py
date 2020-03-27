#Fibonacci Array

n = int(input())
valores = []
for i in range(n):
    v = int(input())
    valores.append(v)
    fib = [0, 1]
    pos1 = 0
    pos2 = 1
    indice = 2
    while len(fib) <= v:
        fib.insert(indice, fib[pos1] + fib[pos2])
        pos1 += 1
        pos2 += 1
        indice += 1
    print("Fib({}) = {}".format(v, fib[v]))