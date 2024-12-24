def main():
    n = int(input())
    smax = 0
    ans = 0
    for i in range(2, 11):
        n1 = n
        s = 0
        while n1 > 0:
            s += n1 % i
            n1 //= i
        if s > smax:
            smax = s
            ans = i
    print(ans)


if __name__ == "__main__":
    main()

