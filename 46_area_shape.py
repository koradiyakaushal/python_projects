import math


class Shape:
    def __init__(self, base, side):
        self.base = base
        self.side = side

    def area(self):
        return self.base * self.side

    def perimeter(self):
        return self.base


class Rectangle(Shape):
    def __init__(self, base, side):
        super(Rectangle, self).__init__(base, side)

    def area(self):
        return 2 * (self.side + self.base)

    def perimeter(self):
        return self.base * self.side


class Square(Shape):
    def __init__(self, base):
        super(Square, self).__init__(base, base)

    def area(self):
        return 4 * self.base

    def perimeter(self):
        return 2 * self.base


class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__(radius, radius)
        self.r = radius

    def area(self):
        return 2 * 22 / 7 * self.r

    def perimeter(self):
        return 2 * 22 / 7 * self.r


class Triangle(Shape):
    def __init__(self, base, side):
        super(Triangle, self).__init__(base, side)

    def area(self):
        return 1 / 2 * (self.base * self.side)

    def perimeter(self, a, b, c):
        return a + b + c


s = Square(5)
print(s.area())
print(s.perimeter())

c = Circle(8)
print(c.area())
print(c.perimeter())

r = Rectangle(5, 6)
print(r.area())
print(r.perimeter())

t = Triangle(3, 5)
print(t.perimeter(6, 8, 9))
print(t.area())
