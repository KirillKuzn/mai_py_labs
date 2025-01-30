class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def length(self, point):
        res = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(res, 2)
    

point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
