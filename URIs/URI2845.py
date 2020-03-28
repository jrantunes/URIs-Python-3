#Party at the North Pole

v = int(input())
val = list(map(int, input().split()))
nums = []
for i in range(v):
    nums.insert(i, val[i])
    
anf = max(nums) + 1
print(anf)