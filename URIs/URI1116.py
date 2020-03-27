#Dividing X by Y

N = int(input())

for i in range(N):
    valores = input().split()
    v1 = int(valores[0])
    v2 = int(valores[1])
    if v2 == 0:
        print("divisao impossivel")
    
    else:
        div = v1 / v2
        print(div)