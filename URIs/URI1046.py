#Game Time

horas = input().split()

a = int(horas[0])
b = int(horas[1])

if a == b:
    print("O JOGO DUROU 24 HORA(S)")

elif a > b:
    t = 24 - (a - b)
    print("O JOGO DUROU {} HORA(S)".format(t))

else:
    t = abs(a - b)
    print("O JOGO DUROU {} HORA(S)".format(t))