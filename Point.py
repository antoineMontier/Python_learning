from math import sqrt


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y

    def __add__(self, p):
        return Point(p.get_x() + self._x, p.get_y() + self._y)

    def __mul__(self, p):
        return Point(p.get_x() * self._x, p.get_y()*self._y)

    def __str__(self):
        return "(%d, %d)" % (self._x, self._y)

    def __eq__(self, p) -> bool:
        return p.get_x() == self._x and p.get_y() == self._y

    def __sub__(self, p):
        return Point(self._x - p.get_x(), self._y - p.get_y())

    def __truediv__(self, p):
        return Point(self._x / p.get_x(), self._y / p.get_y())

    def distance(self, p):
        return sqrt((self._x - p.get_x())*(self._x - p.get_x()) + (self._y - p.get_y())*(self._y - p.get_y()))


a = Point(12, 5)
b = Point(10, 5)

print("a =", a, "\nb =", b)
print("a+b =", a+b)
print("a-b =", a-b)

print("a*b =", a*b)
print("a/b =", a/b)

print("a == b :", a == b)

print("dist :", a.distance(b))

