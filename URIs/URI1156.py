#S Sequence II

nums1 = [3]
pos1 = 1
num = 0

nums2 = [2]
pos2 = 1
num2 = 0

while nums1[-1] != 39:
    nums1.insert(pos1, nums1[num] + 2)
    pos1 += 1
    num += 1

while len(nums2) != len(nums1):
    nums2.insert(pos2, nums2[num2] + nums2[num2])
    pos2 += 1
    num2 += 1

frac = []

for i in range(len(nums1)):
    frac.append(nums1[i] / nums2[i])

print("{:.2f}".format(1 + sum(frac)))