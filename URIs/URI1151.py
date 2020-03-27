#Easy Fibonacci

n = int(input())

seq = [0, 1]
indice = 2
pos1 = 0
pos2 = 1
while len(seq) <= n - 1:
    seq.insert(indice, seq[pos1] + seq[pos2])
    indice += 1
    pos1 += 1
    pos2 += 1
a = str(seq).strip("[]")
a = a.replace(",", "")
print(a)

