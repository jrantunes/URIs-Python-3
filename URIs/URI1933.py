#Tri-du

a, b = input().split()
a = int(a)
b = int(b)

if 1 <= a <= 13 and 1 <= b <= 13: 
    
    if a == b:
        c = a 
        print(c)

    elif a > b:
        c = a
        print(c)

    else:
        c = b
        print(c)
