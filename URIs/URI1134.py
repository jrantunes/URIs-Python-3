#Type of Fuel

alcool = []
gasolina = [] 
diesel = []
while True:
    V = int(input())

    if V == 1:
        alcool.append("a")
    
    elif V == 2:
        gasolina.append("g")

    if V == 3:
        diesel.append("d")

    elif V == 4:
        break
    
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(len(alcool), len(gasolina), len(diesel)))