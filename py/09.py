# Dictionary Basics (JSON)

# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A",
#     "courses": ["Math", "Science", "English"]
# }

# # Accessing and modifying 
# print(student["name"])
# print(student.get("gender"))
# print(student["age"])

# student["age"] = 21                    # Modify value
# student["email"] = "alice@gmail.com"   # Add new key-value 

# print(student["age"])
# print(student["email"])


# keys = student.keys()         # Get all keys
# values = student.values ()    # Get all values
# items = student.items()       # Get all key-value pairs

# print(keys)
# print(values)
# print(items)


# # Iterating through dictionaries 
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")


# # Nested dictionaries 
# company = {
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "jane": {"age": 25, "department": "HR"}
#     },
#     "departments": ["IT", "HR", "Finance"]
# }

# print(company["employees"].items())
# print(company["departments"])


# Ex: 
student_record = {"student_001": {"name": "John", "age": 19, "major": "Computer Science", "grades": [85, 92, 78]},
                  "student_002": {"name": "Sarah", "age": 20, "major": "Biology", "grades": [90, 88, 95]}
}

# Add a new "student_003" 
student_record["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

# Update John's age to 20 
student_record["student_001"]["age"] = 20

print(student_record)


# Loop through the dictionary and print each student's ID, name, and major
for id, student_info in student_record.items():
    name = student_info["name"]
    major = student_info["major"]
    print(f"Student ID: {id}, Name: {name}, Major: {major}")

