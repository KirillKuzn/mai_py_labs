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
    
    def get_pos(self):
        return (round(min(self.x1, self.x2), 2), round(max(self.y1, self.y2), 2))
    
    def get_size(self):
        return (round(self.x, 2), round(self.y, 2))
    
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, w, h):
        self.x = w
        self.y = h