n = int(input("enter num"))

orignal = n
sum = 0

while n > 0:
   digit = n % 10
sum = sum + digit**3
n = n//10




if orignal == sum:
   print("armstronng")
else:
   print("not armstrong") 