#The strike stops or continues?

r = int(input())

G = []
V = []

for i in range(r):
    gv = input().split()
    if gv[0] == "G":
        G.append(int(gv[1])) 

    elif gv[0] == "V":
        V.append(int(gv[1]))

if sum(G) > sum(V):
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")