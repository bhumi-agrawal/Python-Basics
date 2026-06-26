n = [2,2,3,4]
seen = []

for num in n:
    if  num not in seen:
        print(num)
        seen.append(num)