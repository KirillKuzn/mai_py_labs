class Rectangle:

    def __init__(self, p1, p2):
        self.x1 = min(p1[0], p2[0])
        self.y1 = max(p1[1], p2[1])
        self.x2 = max(p1[0], p2[0])
        self.y2 = min(p1[1], p2[1])
        self.width = self.x2 - self.x1
        self.height = self.y1 - self.y2

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)
    
    def area(self):
        return round(self.width * self.height, 2)
    
    def get_pos(self):
        return (round(self.x1, 2), round(self.y1, 2))
    
    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))
    
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, w, h):
        self.width = w
        self.height = h
        self.x2 = self.x1 + w
        self.y2 = self.y1 - h

    def turn(self):
        d = (self.width - self.height) / 2

        self.x1 += d
        self.x2 -= d
        self.y1 += d
        self.y2 -= d

        self.width, self.height = self.height, self.width

    def scale(self, factor):
        self.x1 -= self.width / 2 * (factor - 1)
        self.y1 += self.height / 2 * (factor - 1)
        self.x2 += self.width / 2 * (factor - 1)
        self.y2 -= self.height / 2 * (factor - 1)

        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)
