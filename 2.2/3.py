p = int(input())
v = int(input())
t = int(input())
if p > max(v, t):
    print('Петя')
elif v > max(p, t):
    print('Вася')
else:
    print('Толя')
