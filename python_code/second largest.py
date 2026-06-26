num = [10,20,30,40]

large = num[0]
slarge = num[0]

for nums in num:
   if nums > large:
      slarge = large
      large = nums
   elif nums > slarge:
    slarge = nums
      
print(large)
print(slarge)     



