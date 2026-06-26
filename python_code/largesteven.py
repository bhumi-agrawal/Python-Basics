n = [2,3,4,6]
large = n[0]


for nums in n:
    if nums % 2 == 0 and nums  > large:
            large = nums
print(large)