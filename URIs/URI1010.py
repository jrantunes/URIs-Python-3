#Simple Calculate

#criar uma função p/ calcular o valor a ser pago
def valor(n1, v1, n2, v2):
    res = n1 * v1 + n2 * v2
    return res

#ler o codigo de uma peça p1 (cp1)/número de peças(np1)/o valor de cada peça(vp1)
p1 = input().split()
cp1 = int(p1[0])
np1 = int(p1[1])
vp1 = float(p1[2])

#repetir o processo com p2
p2 = input().split()
cp2 = int(p2[0])
np2 = int(p2[1])
vp2 = float(p2[2])

#chamar a função
res = valor(np1, vp1, np2, vp2)

#resultado
print("VALOR A PAGAR: R$ {:.2f}".format(res))