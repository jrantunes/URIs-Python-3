#Converting to Hexadecimal

num = int(input())
hx = list(hex(num))

del hx[0], hx[0]

hx = ",".join(hx).strip("[]")
hx = hx.replace(",", "")
hx = hx.upper()

print(hx)
