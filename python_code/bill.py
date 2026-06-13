unit = int(input("enter electricity bill"))

if unit <= 100:
    bill = unit*5
elif unit <=200:
    bill = unit*8
else:
    bill = unit*10
    print("final bill =" ,bill)
