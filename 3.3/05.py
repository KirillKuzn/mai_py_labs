numbers = [1, 2, 3, 4, 5]
ans = set([i for i in numbers if i ** 0.5 == int(i ** 0.5)])
print(ans)