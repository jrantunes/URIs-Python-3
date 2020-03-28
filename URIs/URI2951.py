#The Return of The King

v = list(map(int, input().split()))
qtde = v[0]
amzde_nec = v[1]

runas = []
valores = []

for i in range(qtde):
    rv = input().split()
    r = rv[0]
    v = int(rv[1])

    runas.append(r)
    valores.append(v)

x = int(input())

a = list(input().split())

recit = []
for i in range(x):
    recit.insert(i, a[i])

indices = []

for i in range(len(recit)):
    g = runas.index(recit[i])
    indices.append(g)

pontos = []

for i in indices:
    pontos.append(valores[i])

print(sum(pontos))
if sum(pontos) >= amzde_nec:
    print("You shall pass!")

else:
    print("My precioooous")