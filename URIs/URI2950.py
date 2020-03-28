#The Two Towers

valores = input().split()
N = int(valores[0])
X = int(valores[1])
Y = int(valores[2])

x_y = X + Y
div = N / x_y

print("{:.2f}".format(div))