#Age in Days

dias = int(input())

ano = dias // 365
mes = (dias % 365) // 30
dia = (dias % 365) % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dia))