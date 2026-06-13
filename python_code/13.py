a = int(input("1"))
b = int(input("2"))
c = int(input("3"))

if (a>=b and a<=c) or (a<=b and a>=c):
    print(a)
elif(b>=a and b<=c) or (b<=a and b>=c):
    print(b)
else:
    print(c)