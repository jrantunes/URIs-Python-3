#Final Thesis of Christmas Depression

valores_ED = input().split()

E = int(valores_ED[0])
D = int(valores_ED[1])
mt_bem = D - 3
trabalho_filho = D - 2
add = D + 2
if E > D :
    print("Eu odeio a professora!")

elif 0 < E < 25 and 0 < D < 25:
    if E <= mt_bem:
        print("Muito bem! Apresenta antes do Natal!")

    elif E >= trabalho_filho:
        print("Parece o trabalho do meu filho!")

        if add <= 24:
            print("TCC Apresentado!")
    
        elif add > 24:
            print("Fail! Entao eh nataaaaal!")