def main():
    n = int(input())
    s = 0
    for i in range(n):
        num = int(input())
        cmax = 0
        while num > 0:
            cmax = max(cmax, num % 10)
            num //= 10
        s += cmax * 10 ** (n - 1 - i)
    print(s)


if __name__ == "__main__":
    main()