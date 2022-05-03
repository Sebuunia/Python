h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))

BMI = w / (h/100)**2

print("Your Body Max Index is", BMI)

if BMI <= 18.5:
    print("You are underweight!")
elif BMI <= 24.9:
    print("You are healthy!")
elif BMI <= 30.9:
    print("You are overweight!")
else:
    print("Error...")