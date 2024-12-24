p = int(input())
p1 = p2 = 0
p1 += p % 10
p = p // 10
p1 += p % 10
p2 = p % 10 + p // 10
if p1 > p2:
    p = int(str(p1) + str(p2))
else:
    p = int(str(p2) + str(p1))
print(p)