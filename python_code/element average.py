n = [10,20,20,40,50]
avg = n[0]
for num in n:
    avg = sum(n) / len(n)
    if num > avg:
        print(num)
   
