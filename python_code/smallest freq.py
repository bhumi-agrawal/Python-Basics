n = [5,2,2,8,8,1,1]
se = {}
for num in n:
    if num in se:
        se[num] += 1
    else:
        se[num] = 1

repated = []
for key in se:
   if se[key] > 1:
      repated.append(key)
print(max(repated))      