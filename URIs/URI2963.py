#Buffoon

n = int(input())

votos = []
for i in range(n):
    v = int(input())
    votos.append(v)

if votos[0] >= max(votos):
    print("S")
else:
    print("N")