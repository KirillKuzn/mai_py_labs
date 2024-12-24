a = int(input())
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
c = [a1, a2, a3]
c.sort()
amax = c[2] * 10 + c[1]
if c[0] == 0:
    amin = c[1] * 10
else:
    amin = c[0] * 10 + c[1]
print(amin, amax)