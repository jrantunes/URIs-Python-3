#Sphere

#criar uma função calcular o volume de uma esfera((4/3) * pi) * r ** 3) e imprima o resultado.
def volume(raio):
    res = ((4 / 3) * 3.14159) * raio ** 3
    print("VOLUME = {:.3f}".format(res))
    return volume

#ler o raio(float)
r = float(input())

#chamar a função
volume(r)
