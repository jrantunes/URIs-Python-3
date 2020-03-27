#Sum of Consecutive Odd Numbers II

n = int(input())

for i in range(n):
    
    valores = input().split()
    n1 = int(valores[0])
    n2 = int(valores[1])
    
    lista = [n1, n2]

    lista.sort()
    v1 = lista[0]
    v2 = lista[1]
    
    impares = []

    for n in range(v1 + 1, v2):
        if n % 2 == 1:
            impares.append(n)

    print(sum(impares))