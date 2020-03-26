#Distance Between Two Points

import math
#separar os (x) e (y) dos pontos (a) e (b)
a = input().split()
xa = float(a[0])
ya = float(a[1])

b = input().split()
xb = float(b[0])
yb = float(b[1])

#calcular a distancia( raiz(xb - xa ** 2 + yb - ya ** 2) )
d = math.sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))
print("{:.4f}".format(d))