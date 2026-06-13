income = int(input("enter amount of income"))
if income <= 300000:
    tax = 0
    print(" no tax")
elif income <= 700000:
     tax = income*0.10
     print  ( "tax")   
else:
     tax = income*0.20
     print("tax")