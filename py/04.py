# age = 18

# if age >= 18: 
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# score = 85

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else: 
#     grade = "F"

# print(f"Your grade is: {grade}")


# user_age = 25
# has_license = True

# if user_age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")


# day = "Saturday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else: 
#     print("It's a weekday.")
          

# weather = "sunny"
# temperature 75

# if weather == "sunny":
#     if temperature > 70:
#         print("It's sunny and warm.")
#     else: 
#         print("It's sunny but cool.")


# Exercise:

while True: 
    try:
        kg = float(input("What's your weight in kg? "))
        if kg > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        m = float(input("What's your height in meters? "))
        if m > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

bmi = kg / (m ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.") 