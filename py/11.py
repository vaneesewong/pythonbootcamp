# # Error Handling (Can use Exception for most cases)

# # Basic exception handling (Eg. Login Page)
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:   
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError: 
#     print("Cannot divide by zero!")


# # Basic exception handling (Eg. Login Page) (Can replace ValueError with Exception)
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except Exception:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError: 
#     print("Cannot divide by zero!")


# # Using else and finally 
# try: 
#     file = open("data.txt", "r")
# except FileNotFoundError:   
#     print("File not found!")
# else:
#     # Executes if no exception occured
#     content = file.read()
#     print(f"File read successfully: {content}.")
# finally:
#     # Always executes 
#     if "file" in locals() and not file.closed:
#         file.close()
#         print("Cleanup completed")


# Using else and finally (Can replace FileNotFoundError with Exception)
try: 
    file = open("data.txt", "r")
except Exception as e:
    print(f"File not found! {e}")
else:
    # Executes if no exception occured
    content = file.read()
    print(f"File read successfully: {content}.")
finally:
    # Always executes 
    if "file" in locals() and not file.closed:
        file.close()
        print("Cleanup completed")


# # Raising exceptions 
# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     if age > 150:
#         raise ValueError("Age seems unrealistic.")
#     return True
# try:
#     validate_age(170)
# except ValueError as e:
#     print(f"Validation error: {e}")


# Raising exceptions (Can replace FileNotFoundError with Exception)
def validate_age(age):
    if age < 0:
        raise Exception("Age cannot be negative.")
    if age > 150:
        raise Exception("Age seems unrealistic.")
    return True
try:
    validate_age(180)
except Exception as e:
    print(f"Validation error: {e}")
