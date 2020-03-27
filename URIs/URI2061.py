#Closing Tabs
 
a, i = input().split()
a = int(a)
i = int(i)
for x in range(i):
  esc = input()
  if esc == "fechou":
    a -= 1
    a += 2
  else:
    a -= 1

print(a)