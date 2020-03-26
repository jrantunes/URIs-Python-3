#Area

#criar uma função para calcular as areas do triangulo ret., circulo, trapezio, quadrado, retangulo.
def areas(va, vb, vc):
    #area do triangulo ret. (b * h / 2) usando (a) como base-b e (c) como altura-h
    area_triangulo = (va * vc) / 2
    print("TRIANGULO: {:.3f}".format(area_triangulo))

    #area do circulo (pi * r ** 2) usando (c) como raio
    area_circulo = 3.14159 * (vc ** 2)
    print("CIRCULO: {:.3f}".format(area_circulo))

    #area do trapezio ((b + b * h) / 2) tendo (a) e (b) por bases-b e c por altura-h
    area_trapezio = ((va + vb) * vc) / 2
    print("TRAPEZIO: {:.3f}".format(area_trapezio))

    #area do quadrado (l ** 2) tendo (b) como lado
    area_quadrado = vb ** 2
    print("QUADRADO: {:.3f}".format(area_quadrado))

    #area do retangulo (b * h) tendo (a) e (b) como lados
    area_retangulo = va * vb
    print("RETANGULO: {:.3f}".format(area_retangulo))


#ler 3 valores(float) a, b, c na mesma linha
valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

#chamar a função
areas(a, b, c)