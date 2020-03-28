#Polyglot Parrot

while True:
    try:
        s = input()
        if s == "nenhuma":
            print("portugues")
        elif s == "as duas":
            print("caiu")
        elif s == "esquerda":
            print("ingles")
        elif s == "direita":
            print("frances")
    except EOFError:
        break