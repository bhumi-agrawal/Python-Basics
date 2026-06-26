n = [2,3,3,4,5]
count = 0
seen = []
for num in n:
    if num  in seen:
        print(num)
    else:

        seen.append(num)