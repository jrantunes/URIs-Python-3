#Santa's toys

f = []
m = []

v = int(input())

for i in range(v):
    n, g = input().split()
    if g == "F":
        f.append(g)
    elif g == "M":
        m.append(g)

print(len(m), "carrinhos\n{} bonecas".format(len(f)))