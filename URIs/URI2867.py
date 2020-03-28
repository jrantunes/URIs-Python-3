#Digits

v = int(input())

for i in range(v):
    nums = list(map(int, input().split()))
    quad = nums[0] ** nums[1]
    quad = str(quad)
    print(len(quad))