##Output 7

nums = []

for n in range(97, 122 + 1):
    nums.append(n)

abc = []
for c in range(ord("a"), ord("z") + 1):
    abc.append(chr(c))

for i in range(len(nums)):
    print("{} e {}".format(nums[i], abc[i]))