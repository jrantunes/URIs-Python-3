#Exceeding Z

x = int(input())
z = x - 1
while z <= x:
    z = int(input())
soma = x
qte = 1
while soma < z:
    soma += x + qte
    qte += 1
print(qte)