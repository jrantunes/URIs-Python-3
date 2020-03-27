#Electrical Outlet

t1, t2, t3, t4 = input().split()

t1, t2, t3, t4 = int(t1) - 1, int(t2) - 1, int(t3) - 1, int(t4)

tomadas = [t1, t2, t3, t4]

print(sum(tomadas))