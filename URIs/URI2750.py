#Output 4

nums = []
hexa = []
octo = []

for i in range(0, 15 + 1):
    nums.append(i)

for i in range(len(nums)):
    a = list(oct(nums[i]))
    del a[0]
    del a[0]
    a = ",".join(a)
    a = a.replace(",", "")
    a = int(a)
    octo.append(a)

for i in range(len(nums)):
    b = list(hex(nums[i]))
    del b[0]
    del b[0]
    b = ",".join(b)
    v = b.upper()
    hexa.append(v)

print("-" * 39)
print("|  decimal  |  octal  |  Hexadecimal  |")
print("-" * 39)
print("|      {}    |    {}    |       {}       |".format(nums[0], octo[0], hexa[0]))
print("|      {}    |    {}    |       {}       |".format(nums[1], octo[1], hexa[1]))
print("|      {}    |    {}    |       {}       |".format(nums[2], octo[2], hexa[2]))
print("|      {}    |    {}    |       {}       |".format(nums[3], octo[3], hexa[3]))
print("|      {}    |    {}    |       {}       |".format(nums[4], octo[4], hexa[4]))
print("|      {}    |    {}    |       {}       |".format(nums[5], octo[5], hexa[5]))
print("|      {}    |    {}    |       {}       |".format(nums[6], octo[6], hexa[6]))
print("|      {}    |    {}    |       {}       |".format(nums[7], octo[7], hexa[7]))
print("|      {}    |   {}    |       {}       |".format(nums[8], octo[8], hexa[8]))
print("|      {}    |   {}    |       {}       |".format(nums[9], octo[9], hexa[9]))
print("|     {}    |   {}    |       {}       |".format(nums[10], octo[10], hexa[10]))
print("|     {}    |   {}    |       {}       |".format(nums[11], octo[11], hexa[11]))
print("|     {}    |   {}    |       {}       |".format(nums[12], octo[12], hexa[12]))
print("|     {}    |   {}    |       {}       |".format(nums[13], octo[13], hexa[13]))
print("|     {}    |   {}    |       {}       |".format(nums[14], octo[14], hexa[14]))
print("|     {}    |   {}    |       {}       |".format(nums[15], octo[15], hexa[15]))
print("-" * 39)