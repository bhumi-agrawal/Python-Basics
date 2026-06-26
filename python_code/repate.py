n = [5,2,3,2,5]
seen = []
for num in n:
    if num in seen:
        print(num)
        break
    else:
        seen.append(num)