n = int(input("enter num"))
even = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even = even + digit

    n = n // 10

print(even)