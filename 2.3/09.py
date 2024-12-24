def main():
    a = int(input())
    f = 1
    if a == 0:
        print(1)
    else:
        for i in range(1, a + 1):
            f *= i
        print(f)


if __name__ == "__main__":
    main()