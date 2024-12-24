a = int(input())
b = int(input())
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
s = [a1, a2, b1, b2]
s.sort()
c1 = s[3]
c3 = s[0]
c2 = (s[1] + s[2]) % 10
print(c1 * 100 + c2 * 10 + c3)
