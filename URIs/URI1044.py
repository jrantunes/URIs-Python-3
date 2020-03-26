#Multiples

multiplos = []
valores = input().split()

v1 = int(valores[0])
v2 = int(valores[1])

nums = [v1, v2]

a = abs(nums[0])
b = abs(nums[1])

nums_abs = [a, b]
nums_abs.sort()

a = nums_abs[0]
b = nums_abs[1]

for i in range(b + 1):
    if a * i == b:
        multiplos.append(i)

if b / a in multiplos:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")