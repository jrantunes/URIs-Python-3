#A idade de Dona Mônica

m = int(input())
a = int(input())
b = int(input())
filhos = [a, b]

if 40 <= m <= 110 and 1 <= a < m and 1 <= a < m and a != b:
    c = m - (a + b)
    filhos.append(c)
    print(max(filhos))

else:
    exit()