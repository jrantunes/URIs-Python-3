#The Bad Vibes Walk

v = list(map(int, input().split()))
linhas = v[0] 
col = v[1]

v = []
d = []

for i in range(linhas):
    val = input().split()
    teste = []
    for n in range(col):
        teste.insert(n, val[n])
    for t in teste:
        a = ",".join(t)
        a = a.split(",")
        if a[1] == "V":
            v.append(t)
        else:
            d.append(t)
v.sort()
v.reverse()
d.sort()
d.reverse()

for l in v:
    print(l)
for m in d:
    print(m)