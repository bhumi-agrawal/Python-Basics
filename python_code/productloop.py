n = int(input("enter num"))
product = 1


while n > 0:
    digit = n % 10
    product = product*digit
    n  = n // 10

print(product) 