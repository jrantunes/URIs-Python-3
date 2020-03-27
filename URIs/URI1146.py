#Growing Sequences

while True:
    sequencia = []
    x = int(input())

    if 0 < x:
        for i in range(1, x + 1):
            sequencia.append(i)

        a = str(sequencia).strip("[]")
        a = a.replace(",", "")
        print(a)

    else: 
        break