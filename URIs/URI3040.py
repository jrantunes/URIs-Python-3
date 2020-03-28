#The Christmas Tree

v = int(input())

for i in range(v):
    vs = list(map(int, input().split()))
    a = vs[0]
    b = vs[1]
    c = vs[2]

    if a in range(200, 300 + 1) and b >= 50 and c >= 150:
        print("Sim")
    else:
        print("Nao")