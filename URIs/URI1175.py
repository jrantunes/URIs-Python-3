#Array change I

valores = []
for i in range(20):
    v = int(input())
    valores.append(v)
n = 0
m = -1
while n <= 9:
    valores[n], valores[m] = valores[m], valores[n]
    n += 1
    m -= 1 
for i in range(len(valores)):
    print("N[{}] = {}".format(i, valores[i]))