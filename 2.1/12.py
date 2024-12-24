def f(x, y):
    sx, sy = str(x), str(y)
    res = ''
    for i in range(1, min(len(sx), len(sy)) + 1):
        res += str((int(sx[-i]) + int(sy[-i])) % 10)
    if len(sx) == len(sy):
        return int(res[::-1])
    elif len(sx) > len(sy):
        return int(sx[0] + res[::-1])
    else:
        return int(sy[0] + res[::-1])

        
a = int(input())
b = int(input())
print(f(a, b))