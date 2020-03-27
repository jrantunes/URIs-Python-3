#Even Between five Numbers

pares = []
for i in range(5):
    valores = int(input())
    if valores % 2 == 0:
        pares.append(valores)
print("{} valores pares".format(len(pares)))
