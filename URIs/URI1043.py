#Triangle

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

abs_ab = abs(A - B)
abs_ac = abs(A - C)
abs_bc = abs(B - C)

if abs_bc < A < B + C and abs_ac < B < A + C and abs_ab < C < A + B:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))

else:
    area_trapezio = (A + B) * C / 2
    print("Area = {:.1f}".format(area_trapezio))