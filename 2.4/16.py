def main():
    n = int(input())
    w = int(input())
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if y < n:
                print(f"{y * x: ^{w}}", end='|')
            else:
                print(f"{y * x: ^{w}}", end='')
        print()
        if x < n:
            print('-' * (n * (w + 1) - 1))


if __name__ == "__main__":
    main()