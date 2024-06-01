# Shape Hierarchy:
# Create a hierarchy of shapes (e.g., Circle, Rectangle, Triangle) where each shape has common attributes
# (e.g., area, perimeter) and specific attributes/methods.
# Implement polymorphic methods such as calculating area and perimeter for each shape.
from math import pi, sqrt


class Shape:
    """
    Base class for all shapes.

    Attributes:
    - area: area of the shape.
    - perimeter: perimeter of the shape.
    """

    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def calc_area(self):
        """Abstract method to calculate the area."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def calc_perimeter(self):
        """Abstract method to calculate the perimeter."""
        raise NotImplementedError("This method should be implemented in a subclass.")


class Circle(Shape):
    """
    Class representing a circle.

    Additional attributes:
    - radius: radius of the circle.
    """

    def __init__(self, radius):
        area = pi * radius ** 2
        perimeter = 2 * pi * radius
        super().__init__(area, perimeter)
        self.radius = radius

    def calc_area(self):
        return pi * self.radius ** 2

    def calc_perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle.

    Additional attributes:
    - length: length of the rectangle.
    - width: width of the rectangle.
    """

    def __init__(self, length, width):
        area = length * width
        perimeter = 2 * (length + width)
        super().__init__(area, perimeter)
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    """
    Class representing a triangle.

    Additional attributes:
    - base: base length of the triangle.
    - side_a, side_b: lengths of the other two sides.
    - height: height of the triangle.
    """

    def __init__(self, base, side_a, side_b, height):
        area = 0.5 * base * height
        perimeter = base + side_a + side_b
        super().__init__(area, perimeter)
        self.base = base
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    def calc_area(self):
        return 0.5 * self.base * self.height

    def calc_perimeter(self):
        return self.base + self.side_a + self.side_b


# Example Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 4)

print("Circle:")
print("Area:", circle.calc_area())
print("Perimeter:", circle.calc_perimeter())

print("\nRectangle:")
print("Area:", rectangle.calc_area())
print("Perimeter:", rectangle.calc_perimeter())

print("\nTriangle:")
print("Area:", triangle.calc_area())
print("Perimeter:", triangle.calc_perimeter())
