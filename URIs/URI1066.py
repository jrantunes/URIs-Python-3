#Even, Odd, Positive and Negative

positivos = []
pares = []
impares = []
negativos = []
for i in range(5):
    valores = int(input())
    if valores % 2 == 0:
        pares.append(valores)
    
    elif valores % 2 == 1:
        impares.append(valores)

    elif valores > 0:
        positivos.append(valores)
    
    else:
        negativos.append(valores)

print("{} valor(es) par(es)".format(len(pares)))
print("{} valor(es) impar(es)".format(len(impares)))
print("{} valor(es) positivo(s)".format(len(positivos)))
print("{} valor(es) negativo(s)".format(len(negativos)))