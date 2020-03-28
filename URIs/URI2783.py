#Cup Stickers

ncm = input().split()
cn = int(ncm[1])
mn = int(ncm[2])
cx = input().split()
mx = input().split()
c = []
m = []

for i in range(cn):
    c.insert(i, cx[i])

for i in range(mn):
    m.insert(i, mx[i])

falta = []
for carim in c:
    if carim not in m:
        falta.append(carim)

print(len(falta))