#Sum of Consecutive Odd Numbers I

X = int(input())
Y = int(input())

valores = [X, Y]
valores.sort()
impares = []

menor = valores[0]
maior = valores[1]

for i in range(menor + 1, maior):
    if i % 2 != 0:
        impares.append(i)
    else:
        pass

print(sum(impares))