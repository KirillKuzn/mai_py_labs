n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
for i in range(n):
    if (k1 * (n - i) + k2 * i) // n == m:
        print(n - i, i)
        break
