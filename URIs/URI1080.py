#Highest and Position

nums = []
for i in range(100):
    num = int(input())
    nums.append(num)

print(max(nums))
print(nums.index(max(nums)) + 1)