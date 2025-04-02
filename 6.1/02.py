import math
from sys import stdin


for line in stdin:
    nums = list(map(int, line.split()))
    print(math.gcd(*nums))