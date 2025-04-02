import math


x1, y1 = map(float, input().split())
ro, fi = map(float, input().split())
x2 = ro * math.cos(fi)
y2 = ro * math.sin(fi)
print(math.hypot(abs(x1 - x2), abs(y1 - y2)))