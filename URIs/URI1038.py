#Snack

ped_quant = input().split()

pedido = int(ped_quant[0])
quantidade = int(ped_quant[1])

if pedido == 1:
    print("Total: R$ {:.2f}".format(quantidade * 4))

elif pedido == 2:
    print("Total: R$ {:.2f}".format(quantidade * 4.5))

elif pedido == 3:
    print("Total: R$ {:.2f}".format(quantidade * 5))

elif pedido == 4:
    print("Total: R$ {:.2f}".format(quantidade * 2))

else:
    print("Total: R$ {:.2f}".format(quantidade * 1.5))