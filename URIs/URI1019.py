#Time Conversion

N = int(input())

h = 3600
m = 60

hora = N // h
min = N // m
minutos = min % m
segundos = N % m

print("{}:{}:{}".format(hora, minutos, segundos))