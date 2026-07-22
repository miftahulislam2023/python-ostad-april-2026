import math

class Shape:
    def area(self):
        pass # খালি রাখা হলো, চাইল্ড ক্লাস এটি পূরণ করবে

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# পলিমরফিজম টেস্ট
shapes = [Circle(5), Rectangle(4, 6)]

for x in shapes:
    print(f"Area: {x.area():.2f}")

# আউটপুট:
# Area: 78.54
# Area: 24.00