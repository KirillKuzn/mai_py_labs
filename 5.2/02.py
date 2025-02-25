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
    

class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"{(self.x, self.y)}"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    

point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))