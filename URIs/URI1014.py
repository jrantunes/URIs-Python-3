#Consumption

#criar uma função para calcular o consumo medio de um automovel(distancia_percorrida / combustivel gasto)
def consumo(dp, cb):
    res = dp / cb
    print("{:.3f} km/l".format(res))

#ler a distancia percorrida(int)
dist = int(input())

#ler o combustivel gasto(float)
combs = float(input())

#chamar a função usando dist e combs como parametro
consumo(dist, combs)