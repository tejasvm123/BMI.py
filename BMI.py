Weight = float(input("enter your Weight in kg: "))
Height = float(input("enter your Height in cm: "))
Height = Height/100

BMI = Weight/(Height**2)
print("your BMI is: ",BMI)

if(BMI>0):
    if(BMI<=16):
        print("you are severly underweight")
    elif(BMI >= 15 and BMI < 18.5):
        print("you are underweight")
    elif(BMI >= 18.5 and BMI < 25):
        print("you are healthy")
    elif(BMI >= 25 and BMI < 30):
        print("you are overweight")
    else: print("you are severly overweight")
else:("enter valid details")

    

    
    


    
