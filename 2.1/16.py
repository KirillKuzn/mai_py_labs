a = int(input())
b = int(input())
c = int(input())
res = str(abs(a - b) / c)
dot = res.index('.')
if res[dot + 1] == res[-1]:
    res += '0'
    print(res)
else:
    res = float(res)
    print(round(res, 2))
