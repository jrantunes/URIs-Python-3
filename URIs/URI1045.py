#Triangle Types

valores = input().split()

v1 = float(valores[0])
v2 = float(valores[1])
v3 = float(valores[2])

nums = [v1, v2, v3]
nums.sort()
nums.reverse()

A = nums[0] 
B = nums[1]
C = nums[2]

A_QUAD = A ** 2
BC_QUAD = (B ** 2) + (C ** 2)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
    exit()

else:    

    if A_QUAD == BC_QUAD:
        print("TRIANGULO RETANGULO")
    
    elif A_QUAD > BC_QUAD:
        print("TRIANGULO OBTUSANGULO")
    
    if A_QUAD < BC_QUAD:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")

    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")