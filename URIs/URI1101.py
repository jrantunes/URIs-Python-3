#Sequence of Numbers and Sum

while True:
    nums = []
    valores = input().split()
    valores.sort()
    v1 = int(valores[0])
    v2 = int(valores[1])
    if v1 > 0 and v2 > 0:
        for i in range(v1, v2 + 1):
            nums.append(i)
        a = str(nums).strip("[]")
        a = a.replace(",", "")
        print(a, "Sum={}".format(sum(nums)))

    else:
        break