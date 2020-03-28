#Eearliest Deadline First

v = int(input())

sum = 0.0
for i in range(v):
    c, p = input().split()
    c = float(c)
    p = float(p)
    sum += c / p
if sum <= 1.0:
    print("OK")
else:
    print("FAIL")