#Balloon of Honor

abc = []

for i in range(ord("A"), ord("Z") + 1):
    abc.append(chr(i))

l = input()

print(abc.index(l) + 1)