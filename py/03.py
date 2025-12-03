# Input and Output Validation 

name = input("Enter your name: ")
height = float(input("Enter your height: "))

# Input validation 
while True: 
    try:
        age = int(input("Enter your age: "))
        if age > 0:
           break 
        else: 
           print("Age must be positive!")
    except ValueError:
       print("Please enter a valid number!")

# Output validation 
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")


# Exercise 1: Calculator 

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

# Input validation 
while True:
      operation = input("Enter operation (+, -, *, /): ")

      if operation == "+":
         result = number_1 + number_2
         break

      elif operation == "-":
         result = number_1 - number_2
         break

      elif operation == "*":
         result = number_1 * number_2
         break

      elif operation == "/":
         if number_2 == 0:
            print("Error. Please enter a non-zero divisor.")
            # re-enter number_2
            number_2 = float(input("Re-enter second number: "))
         else: 
            result = number_1 / number_2
            break 

      else: 
         print("Error. Invalid operation. Please try again.") 

# Output validation 
print(f"Result: {result}")


# Exercise 2: Quiz 

score = 0   # intial score 

print("Welcome to the Quiz! ")

answer_1 = input("1. What is my favourite food? ").strip().lower()
if answer_1 == "sushi":
    score = score + 1

answer_2 = input("2. What is my favourite color? ").strip().lower()
if answer_2 == "orange":
   score = score + 1

answer_3 = input ("3. What is my favourite hobby? ").strip().lower()
if answer_3 == "playing piano":
   score = score + 1

# Show final score 
print(f"Your final score is {score} out of 3.") 