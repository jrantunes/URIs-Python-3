#Elf Time

falta = int(input())
a, b = input().split()
a = int(a)
b = int(b)

tempo = a + b

if tempo <= falta:
    print("Farei hoje!")

else:
    print("Deixa para amanha!")