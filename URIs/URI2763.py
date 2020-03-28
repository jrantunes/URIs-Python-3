# CPF Input and Output

cpf = input().replace(".", " ")
cpf = cpf.replace("-", " ")
cpf = cpf.split()

print("{}\n{}\n{}\n{}".format(cpf[0], cpf[1], cpf[2], cpf[3]))
