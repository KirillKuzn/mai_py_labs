def main():
    n = int(input())
    c = 0
    for i in range(n):
        a = int(input())
        if str(a) == str(a)[::-1]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()