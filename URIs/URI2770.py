#Board Size

while True:
    try:
        x, y, m = input().split()
        x = int(x)
        y = int(y)
        m = int(m)

        for i in range(m):
            xi, yi = input().split()
            xi = int(xi)
            yi = int(yi)

            if xi <= x and yi <= y or xi <= y and yi <= x:
                print("Sim")
            else:
                print("Nao")

    except EOFError:
        break