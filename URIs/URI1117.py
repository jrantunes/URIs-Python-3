#Score Validation

notas = []

while True:
    nota = float(input())
    
    if len(notas) == 2:
        break

    elif 0 > nota or 10 < nota:
        print("nota invalida")
    
    else:
        notas.append(nota)


media = sum(notas) / len(notas)
print("media = {:.2f}".format(media))