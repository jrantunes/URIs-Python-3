#Array Fill III

n = float(input())

vetor = [n]
pos = 1
m = n
while len(vetor) < 100:
    i = m / 2
    vetor.insert(pos, i)
    pos += 1
    m = i
for v in vetor:
    print("N[{}] = {:.4f}".format(vetor.index(v), v))