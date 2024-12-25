a, b = int(input()), int(input())
ans = [x ** 2 for x in range(min(a, b), max(a, b) + 1)]
print(ans)