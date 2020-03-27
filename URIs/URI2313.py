#Which Triangle

def retangulo(a, b, c):
    if (a ** 2) + (b ** 2) == c ** 2:
        print("Retangulo: S")
        return retangulo
    
    else:
        print("Retangulo: N")
        return retangulo

valores = list(map(int, input().split()))
valores.sort()
a, b, c = valores

if a + b <= c:
    print("Invalido")
    

else:
    if a == b == c:
        print("Valido-Equilatero")
        retangulo(a, b, c)

    elif a != b != c:
        print("Valido-Escaleno")
        retangulo(a, b, c)

    elif a == b or a == c or b == c:
        print("Valido-Isoceles")
        retangulo(a, b, c)