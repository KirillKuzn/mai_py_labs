numbers = [1, 2, 3, 4, 5]
ans = ' - '.join(str(i) for i in sorted(list(set(numbers))))
print(ans)
