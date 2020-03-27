#Grenais

v_i = 0
v_g = 0
empts = 0
grenais = 0

while True:
    i, g = list(map(int, input().split()))
    grenais += 1

    if i == g:
        empts += 1
    elif i > g:
        v_i += 1
    else:
        v_g += 1
    
    if int(input("Novo grenal (1-sim 2-nao)\n")) == 2:
        break
    else:
        pass

print(grenais, "grenais")
print("Inter:{}\nGremio:{}\nEmpates:{}".format(v_i, v_g, empts))

if empts == 1:
    print("Não houve vencedor")
elif v_i > v_g:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")