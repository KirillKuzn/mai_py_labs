rle = [('a', 2), ('b', 3), ('c', 1)]
ans = ''.join(c[0] * c[1] for c in rle)
print(ans)