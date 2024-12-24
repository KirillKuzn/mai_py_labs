p = int(input())
v = int(input())
t = int(input())
if p > max(v, t):
    print('1. Петя')
    if v > t:
        print('2. Вася')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Вася')
if v > max(p, t):
    print('1. Вася')
    if p > t:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')
if t > max(v, p):
    print('1. Толя')
    if v > p:
        print('2. Вася')
        print('3. Петя')
    else:
        print('2. Петя')
        print('3. Вася')        
        