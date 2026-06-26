n = [5,5,2,2,2,7]
fre = {}
for num in n:
    if num in fre:
        fre[num] += 1
    else:
        fre[num] = 1    
count = 0
for key in fre:
    if fre[key] > 1:
       count = count + 1
print(count)    