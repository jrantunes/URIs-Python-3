#Fuel Spent

#a = tempo gasto, b = velocidade media
a, b = int(input()), int(input())

#o carro faz 12 km/l
gasto = (a * b) / 12

print("{:.3f}".format(gasto))