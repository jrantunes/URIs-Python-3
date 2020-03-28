#The Fellowship of the Ring

n = int(input())

racas = []

for i in range(n):
    n, r = input().split()
    racas.append(r)

print("{} Hobbit(s)\n{} Humano(s)\n{} Elfo(s)\n{} Anao(s)\n{} Mago(s)".format(racas.count("X"), racas.count("H"), racas.count("E"), racas.count("A"), racas.count("M")))