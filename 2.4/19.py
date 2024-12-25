def main():
    n = int(input())
    rec = []
    for i in range(n):
        a = []
        for j in range(n):
            x = min(j + 1, n - j)
            y = min(i + 1, n - i)
            a.append(min(x, y))
        rec.append(a)
    indent = max([len(str(max(a))) for a in rec])
    for i in rec:
        for j in i:
            print(f"{' ' * (indent - len(str(j)))}{j}", end=' ')
        print()


if __name__ == "__main__":
    main()