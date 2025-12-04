# Sets 

# fruits = {"apple", "banana", "orange"}
# numbers = {1, 2, 3, 4, 5}

# # Set operations
# fruits.add("grape")          # Add element
# fruits.remove("banana")      # Remove element   
# fruits.discard("kiwi")      # Remove element if exists

# print(fruits) 


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))          # Union
# print(set1.intersection(set2))   # Intersection 
# print(set1.difference(set2))     # Difference

# print(set2.union(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))


# Ex: 
grades = [
    ("Alice", "Math", 85), 
    ("Bob", "Science", 92), 
    ("Alice", "Science", 78), 
    ("Charlie", "Math", 90), 
    ("Bob", "Math", 88), 
    ("Alice", "English", 95)
    ]

unique_students = {student for student, subject, grade in grades}
print(unique_students)

unique_subjects = {subject for student, subject, grade in grades}
print(unique_subjects)

unique_grade = {grade for student, subject, grade in grades}
print(unique_grade)

print(f"Unique Students: {unique_students}")
print(f"Unique Subjects: {unique_subjects}")
print(f"Unique Grades: {unique_grade}") 
