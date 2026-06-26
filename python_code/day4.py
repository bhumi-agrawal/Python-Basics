n = [1,1,1,2,2]
se = {}

for num in n:
    if num in se:
        se[num] += 1

    else:
        se[num] = 1

print(max(se, key=se.get))     


