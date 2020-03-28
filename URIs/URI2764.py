#Date Input and Output

data = input().split("/")
dia = data[0]
mes = data[1]
ano = data[2]

#formato mês/dia/ano
print("{}/{}/{}".format(mes, dia, ano))

#formato ano/mês/dia
print("{}/{}/{}".format(ano, mes, dia))

#formato dia-mês-ano
print("{}-{}-{}".format(dia, mes, ano))