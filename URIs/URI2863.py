#Umil Bolt

while True:
    try:
        v = int(input())

        tentativas = []
        for i in range(v):
            tent = float(input())
            tentativas.append(tent)
        print(min(tentativas))
    except EOFError:
        break