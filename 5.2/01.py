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

    
point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
        