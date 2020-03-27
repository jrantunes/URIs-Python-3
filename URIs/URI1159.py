#Sum of Consecutive Even Numbers

while True:
    x = int(input())
    nums = []
    if x == 0:
        break
    
    for i in range(x, 9999):
        if i % 2 == 0:
            nums.append(i)

            if len(nums) == 5:
                print(sum(nums))
                continue