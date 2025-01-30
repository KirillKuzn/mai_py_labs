class Rectangle:

    def __init__(self, p1, p2):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.x = abs(self.x2 - self.x1)
        self.y = abs(self.y2 - self.y1)

    def perimeter(self):
        return round((self.x + self.y) * 2, 2)
    
    def area(self):
        return round(self.x * self.y, 2)
    

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
