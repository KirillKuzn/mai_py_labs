def main():
    a = int(input())
    a1 = 0
    while a != 0:
        if (a // 10 ** (len(str(a)) - 1)) % 2 == 1:
            a1 *= 10
            a1 += a // 10 ** (len(str(a)) - 1)
        a = a % 10 ** (len(str(a)) - 1)
    print(a1)


if __name__ == "__main__":
    main()