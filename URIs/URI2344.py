#Notas da Prova

n = int(input())

if 0 <= n <= 100:
    if n == 0:
        print("E")

    elif n in range(1, 35 + 1):
        print("D")

    elif n in range(36, 60 + 1):
        print("C")

    elif n in range(61, 85 + 1):
        print("B")

    elif n in range(86, 100 + 1):
        print("A")