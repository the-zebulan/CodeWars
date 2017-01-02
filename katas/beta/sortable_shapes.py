class CustomShape(object):
    def __init__(self, area):
        self.area = area

    def __lt__(self, other):
        return self.area < other.area


Shape = CustomShape


class Square(CustomShape):
    def __init__(self, side):
        super(Square, self).__init__(side ** 2)


class Circle(CustomShape):
    def __init__(self, radius):
        from math import pi
        super(Circle, self).__init__(pi * (radius ** 2))


class Triangle(CustomShape):
    def __init__(self, base, height):
        super(Triangle, self).__init__(0.5 * base * height)


class Rectangle(CustomShape):
    def __init__(self, width, height):
        super(Rectangle, self).__init__(width * height)
