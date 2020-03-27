#C Mais ou Menos?

alim = ["suco de laranja", "morango fresco", "mamao", "goiaba vermelha", "manga", "laranja", "brocolis"]
vit = [120, 85, 85, 70, 56, 50, 34]

while True:
    n = int(input())
    if n == 0:
        break

    else:
        qtde_vit = []
        for i in range(n):
            x = input().split()
            q = int(x[0])
            del x[0]
            x = ",".join(x)
            x = x.replace(",", " ")
            ind = alim.index(x)
            vita = q * vit[ind]
            qtde_vit.append(vita)
        
        if sum(qtde_vit) > 130:
            falta = sum(qtde_vit) - 130
            print("Menos {} mg".format(falta))
            continue

        elif sum(qtde_vit) < 110:
            falta = abs(sum(qtde_vit) - 110)
            print("Mais {} mg".format(falta))
            continue

        elif sum(qtde_vit) in range(110, 130 + 1):
            print("{} mg".format(sum(qtde_vit)))
            continue

         