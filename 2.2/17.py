a = float(input())
b = float(input())
c = float(input())
if a == 0:
    x = 0
    if b != 0:
        x = round((-c) / b, 2)
        print(x)
    else:
        if c == 0:
            print('Infinite solutions')
        else:
            print('No solution')
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = round((- b + d ** 0.5) / (2 * a), 2)
        x2 = round((- b - d ** 0.5) / (2 * a), 2)
        print(min(x1, x2), max(x1, x2))
    if d == 0:
        print(round((-b) / 2 * a, 2))
    if d < 0:
        print('No solution')
                  