#Sum of Consecutive Odd Numbers III

n = int(input())

for i in range(n):
    valores = input().split()
    v1 = int(valores[0])
    v2 = int(valores[1])
    
    soma = 0
    j = 1

    while j <= v2:
        if v1 % 2 != 0:
            soma = soma + v1

            v1 = v1 + 1
            j = j + 1

        if v1 % 2 == 0:
            v1 = v1 + 1

    print(soma)

            
