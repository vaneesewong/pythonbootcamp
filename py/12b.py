# Import function from another file
# To import: from file_name import class_name, function_name, variable_name

from a12 import Person

# Creating objects (instances)
person3 = Person("Vaneese", 27)

# Accessing attributes
print(person3.name) 
print(person3.age)

# Calling methods
print(person3.introduce())
print(person3.have_birthday())

# Class attributes 
print(Person.species) 
print(person3.species)



