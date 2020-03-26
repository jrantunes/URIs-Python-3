#The Greatest

#ler 3 valores(int) na mesma linha e imprimir qual é o maior
valores = input().split()
v1 = int(valores[0])
v2 = int(valores[1])
v3 = int(valores[2])

nums = [v1, v2, v3]

print("{} eh o maior".format(max(nums)))