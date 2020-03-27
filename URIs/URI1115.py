#Quadrant

while True:
    coord = input().split()
    x = int(coord[0])
    y = int(coord[1])

    if x == 0 or y == 0:
        break

    elif x > 0 and y > 0:
        print("primeiro")

    elif x < 0 and y < 0:
        print("terceiro")
    
    elif x < 0 and y > 0:
        print("segundo")

    else:
        print("quarto")

