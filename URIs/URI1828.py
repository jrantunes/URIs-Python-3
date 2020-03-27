#Bazinga!

n = int(input())
for i in range(n):
    e1, e2 = input().split()
    if e1 == e2:
        print("Caso #{}: De novo!".format(i + 1))
    
    elif e1 == "tesoura":
        if e2 == "papel" or e2 == "lagarto":
            print("Caso #{}: Bazinga!".format(i + 1))
        elif e2 == "Spock" or e2 == "pedra":
            print("Caso #{}: Raj trapaceou!".format(i + 1))
    
    elif e1 == "papel":
        if e2 == "pedra" or e2 == "Spock":
            print("Caso #{}: Bazinga!".format(i + 1))
        elif e2 == "tesoura" or e2 == "lagarto":
            print("Caso #{}: Raj trapaceou!".format(i + 1))

    elif e1 == "pedra":
        if e2 == "lagarto" or e2 == "tesoura":
            print("Caso #{}: Bazinga!".format(i + 1))
        elif e2 == "papel" or e2 == "Spock":
            print("Caso #{}: Raj trapaceou!".format(i + 1))

    elif e1 == "lagarto":
        if e2 == "Spock" or e2 == "papel":
            print("Caso #{}: Bazinga!".format(i + 1))
        elif e2 == "pedra" or e2 == "tesoura":
            print("Caso #{}: Raj trapaceou!".format(i + 1))

    elif e1 == "Spock":
        if e2 == "tesoura" or e2 == "pedra":
            print("Caso #{}: Bazinga!".format(i + 1))
        elif e2 == "lagarto" or e2 == "papel":
            print("Caso #{}: Raj trapaceou!".format(i + 1))
