#Multiples of 13

nao_multiplos_13 = []

v1 = int(input())
v2 = int(input())

valores = [v1, v2]
valores.sort()

menor = valores[0]
maior = valores[1]

for i in range(menor, maior + 1):

    if i % 13 > 0 or i % 13 < 0:
        nao_multiplos_13.append(i)

print(sum(nao_multiplos_13))    
    