# Create a class called "Rectangle" with attributes for length and width.
# Add a method to the Rectangle class that calculates and returns the area.
# Create a subclass of Rectangle called "Square" that automatically sets the length and width to be equal.
# Add a method to the Square class that calculates and returns the perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Calculating_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def Calculating_perimeter(self):
        return 4 * self.length

# Rectangle dimensions
length = float(input("Please enter the length of the rectangle: "))
width = float(input(("Please enter the width of the rectangle: ")))
# Create an instance of the Rectangle
my_rectangle = Rectangle(length, width)
print("Area of the rectangle is: ", my_rectangle.Calculating_area())

# Square dimensions
side_length = float(input("Please enter the side length of the square: "))
# Create an instance of the Square
my_square = Square(side_length)
print("Perimeter of the square is: ", my_square.Calculating_perimeter())