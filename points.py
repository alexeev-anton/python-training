from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(point1, point2):
        distance_between_x = point2.x - point1.x
        distance_between_y = point2.y - point1.y
        res = sqrt((distance_between_x * distance_between_x) + (distance_between_y + distance_between_y))
        return res

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(0, 1)
b = Point(2, 3)

print(a == Point(0, 1))

print(a == b)

print(Point.distance(Point(1, 2), Point(3, 4)))

print(Point(1, 2).distance(Point(3, 4)))

print(a.distance(b))
