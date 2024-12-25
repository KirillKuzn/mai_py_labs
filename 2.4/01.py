def main():
    n = int(input())
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            print(y * x, end=' ')
        print()


if __name__ == "__main__":
    main()