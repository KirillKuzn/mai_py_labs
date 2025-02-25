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
    
    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
