#DDD

est = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
dds = [61, 71, 11, 21, 32, 19, 27, 31]
esc = int(input())

if esc in dds:
    print(est[dds.index(esc)])
else:
    print("DDD nao cadastrado")