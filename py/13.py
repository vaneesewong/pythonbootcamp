# Object Oriented Programming 

# Inheritance
class Shape:   # Parent class
    def __init__(self, name):
        self.name = name 

    def area(self):
        return 0

class Circle(Shape):   # Child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")   # Calls the parent's __init__ to set name = "Circle". 
        self.radius = radius 

    def area(self):    # Override parent method 
        return 3.14 * self.radius * self.radius 
    
class Square(Shape):   # Child inherits from Shape 
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    
    def area(self):    # Override parent method 
        return self.side * self.side 

class Hexagon(Shape): 
    def __init__(self, side):
        super().__init__("Hexagon")
        self.side = side

    def area(self):     # Override parent method 
        return (3 * (3**0.5) / 2) * self.side * self.side 
    
# Both Circle and Square inherit 'name' attribute from Shape 
circle = Circle(5)
square = Square(4)
hexagon = Hexagon(5)

print(circle.name)   # "Circle" (inherited from Shape)
print(square.name)   # "Square" (inherited from Shape)
print(hexagon.name)  # "Hexagon" (inherited from Shape)

print(circle.area())
print(square.area())
print(hexagon.area())



# Polymorphism (continue after Inheritance)
def print_area(shape):    # Takes any Shape
    print(f"{shape.name} area: {shape.area()}")

# Same method call, different behaviors
print_area(circle)  
print_area(square)  

# # Or with a list 
# shapes = [Circle(3), Square (5), Circle(2)]
# for shape in shapes:
#     print_area(shape)    # Same code, different results 