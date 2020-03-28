#Jogo dos copos

def troca(lista1, lista2):
    for l in lista1:
        if l == 1:
            lista2[0], lista2[1], lista2[2] = lista2[1], lista2[0], lista2[2]
        elif l == 2:
            lista2[0], lista2[1], lista2[2] = lista2[0], lista2[2], lista2[1]
        elif l == 3:
            lista2[0], lista2[1], lista2[2] = lista2[2], lista2[1], lista2[0]
    return lista2

v = int(input())
cup = str(input())

pos = ["A", "B", "C"]
cups = ["A", "B", "C"]
moves = []

for i in range(v):
    move = int(input())
    moves.append(move)
    
a = troca(moves, cups)

print(pos[a.index(cup)])