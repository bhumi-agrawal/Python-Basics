lpyear = input("enter a year")

if lpyear % 400 == 0:
    print("leap year")
elif lpyear % 100 == 0:
    print("not leap")  
elif lpyear % 4 == 0:
    print("leap year")
else:
    print("not leap year")