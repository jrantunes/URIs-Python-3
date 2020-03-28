#Avoiding Rain

v = int(input())

C = E = c = e = 0

for i in range(v):
    sd, sn = input().split()
    if sd == "chuva":
        e += 1
        if c > 0:
            c -= 1
        else:
            C += 1
    if sn == "chuva":
        c += 1
        if e > 0:
            e -= 1
        else:
            E += 1
        
print(C, E)