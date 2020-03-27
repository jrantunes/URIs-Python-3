#Taxes

salario = float(input())
r = 0
if 0 <= salario <= 2000:
    print("Isento")
else:
    if 2000 < salario <= 3000:
        resto = salario - 2000
        r = resto * 0.08
    elif 3000 < salario <= 4500:
        resto = salario - 3000
        r = (resto * 0.18) + (1000 * 0.08)
    else:
        resto = salario - 4500
        r = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(r))