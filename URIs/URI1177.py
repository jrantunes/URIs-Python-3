#Array Fill II

n = int(input())
nums = []
for i in range(n):
    nums.append(i)
r = []
while len(r) < 1000:
    for num in nums:
        r.append(num)
for m in range(1000):
    print("N[{}] = {}".format(m, r[m]))