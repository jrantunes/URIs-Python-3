#Ages

teste = []
while True:
    n = int(input())
    if n >= 0:
        teste.append(n)
    else:
        print("{:.2f}".format(sum(teste) / len(teste)))
        break