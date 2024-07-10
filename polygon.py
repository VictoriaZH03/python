class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self, length):
        return int(self.sides * length)

    def area(self, apothem, length):
        return 0.5 * apothem * self.perimeter(length)

class Triangle(Polygon):
    
    def area(self, height, length):
        return (length * height) / 2

class Rectangle(Polygon):

    def perimeter(self, len_a, len_b):
        return 2 * (len_a + len_b)

    def area(self, len_a, len_b):
        return len_a * len_b

square = Polygon(4)
print(f"The square has {square.sides} sides, each of 10 cm length.")
print(f"Perimeter: {square.perimeter(10)} cm, Area: {square.area(6, 10)} cm^2")

tr = Triangle(3)
print(f"The triangle has {tr.sides} sides, each of 5 cm length.")
print(f"Perimeter: {tr.perimeter(5)} cm, Area: {tr.area(8, 5)} cm^2")

rect = Rectangle(4)
print(f"The rectangle has {rect.sides} sides, where a is 7 cm, b is 9 cm.")
print(f"Perimeter: {rect.perimeter(7, 9)} cm, Area: {rect.area(7, 9)} cm^2")