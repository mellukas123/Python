#Write program that calculates body mass index
#(bmi = weight / (height*height))

user_weight = float(input("Enter your weight in kilograms: "))
user_height = float(input("Enter your height in meters: "))

bmi = user_weight / (user_height ** 2)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi < 30.0:
    print("Overweight")
elif bmi > 30.0:
    print("Obese")