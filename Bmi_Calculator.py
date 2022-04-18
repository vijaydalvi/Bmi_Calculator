height=float(input("Enter Your Height Cm:-"))
weight=float(input("Enter Your Weight in Kg:-"))
height=height/100
BMI=weight/(height*height)
print("Your Body Mass Index is:",BMI)
if BMI>0:
    if BMI<=16:
        print("You are Severely Underweight")
    elif BMI<=18.5:
        print("You are Underweight")
    elif BMI<=25:
        print("You are Healthy")
    elif BMI<=30:
        print("You are Overweight")
    else:
        print("You are Severely Overweight")
else:
    print("You have entered invalid Details")