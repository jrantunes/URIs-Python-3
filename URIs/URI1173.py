#Array fill I

n = int(input())

vetor = [n]
indice = 1
pos = 0

while len(vetor) < 10:
    vetor.insert(indice, 2 * vetor[pos])
    indice += 1
    pos += 1

for i in range(10):
    print("N[{}] = {}".format(i, vetor[i]))