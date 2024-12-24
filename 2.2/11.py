a = int(input())
s = [a // 100, a // 10 % 10, a % 10]
if max(s) + min(s) == 2 * (sum(s) - max(s) - min(s)):
    print('YES')
else:
    print('NO')