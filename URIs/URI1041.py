#Coordinates of a Point
 
valores = input().split()

x = float(valores[0])
y = float(valores[1])

if x == 0 and y == 0:
    print("Origem")

elif x == 0: 
    print("Eixo Y")

elif y == 0: 
    print("Eixo X")

elif y > 0 and x > 0:
    print("Q1")

elif y < 0 and x < 0:
    print("Q3")

elif y < 0 and x > 0:
    print("Q4")

else:
    print("Q2")