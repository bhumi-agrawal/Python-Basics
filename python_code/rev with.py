n = [1,2,3,4,5,6]
even = []
for num in n:
    if num % 2 == 0:
        even.append(num)



even.reverse()


j = 0


for i in range(len(n)):
   if n[i] % 2 == 0:
     n[i] = even[j]
     j += 1

print(n)