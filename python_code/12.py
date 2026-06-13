a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
c = int(input("enter 3rd number"))
d = int(input("enter 4th number"))

if a>=b and a>=c and a>=d:
    print(a)
elif b>=a and b>=c and b>=d:
    print(b)
elif c>=a and c>=b and c>=d:
    print(c)
else:
    print(d)
 