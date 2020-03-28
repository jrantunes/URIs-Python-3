#How Much Cassava?

gramas_participantes = [300, 1500, 600, 1000, 150]
lista = []
for i in range(5):
    n = int(input())
    vezes = n * gramas_participantes[i]
    lista.append(vezes)

print(sum(lista) + 225)