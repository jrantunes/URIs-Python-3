#Whose Turn Is It?

n = int(input())

for i in range(n):
    name1, e1, name2, e2 = input().split()
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)

    if (n1 + n2) % 2 == 0:
        if e1 == "PAR":
            print(name1)
        else:
            print(name2)
    else:
        if e1 == "IMPAR":
            print(name1)
        else:
            print(name2)