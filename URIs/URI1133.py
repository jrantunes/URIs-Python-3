#Rest of a Division

resto_3_2 = []
X = int(input())
Y = int(input())
valores = [X, Y]
valores.sort()
menor = valores[0] + 1
maior = valores[1]

for i in range(menor, maior):
    if i % 5 == 2 or i % 5 == 3:
        resto_3_2.append(i)

for n in resto_3_2:
    print(n)