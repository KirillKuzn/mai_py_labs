def main():
    n = int(input())
    s = 0
    for i in range(n):
        a = int(input())
        while a != 0:
            s += a % 10
            a //= 10
    print(s)


if __name__ == "__main__":
    main()