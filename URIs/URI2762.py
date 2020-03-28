#Input and Output 6

a = list(map(int, input().split(".")))
a.reverse()
b = str(a).strip("[]")
b = b.replace(" ", "")
b = b.replace(",", ".")
print(b)