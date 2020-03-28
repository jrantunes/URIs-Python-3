#Album of the Cup

def repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)

    return l

total = int(input())
compradas = int(input())

fig = []

for i in range(compradas):
    f = int(input())
    fig.append(f)

a = repetidos(fig)

falta = total - len(a)
print(falta)