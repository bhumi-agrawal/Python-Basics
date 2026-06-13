n = int(input("1"))
if n > 0:
    if n % 2 == 0:
        print("positive even")
    else:
        print("positive odd")
elif n<0:
       if n % 2== 0:
        print("negative even")
       else:
        print("negative odd")
else:
    print("zero")
 