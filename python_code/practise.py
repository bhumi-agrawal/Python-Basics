num = [2, 2, 3, 4]
seen = []

for n in num:
    if num.count(n) > 1 and n not in seen:
        print(n)
        seen.append(n)