def main():
    n = int(input())
    d = {}
    for i in range(n):
        f = input()
        if f in d:
            d[f] += 1
        else:
            d[f] = 1
    ans = 0
    for f in d:
        if d[f] > 1:
            ans += d[f]
    print(ans)


if __name__ == "__main__":
    main()