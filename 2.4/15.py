def main():
    n = int(input())
    m = int(input())
    rec = []
    for i in range(n):
        x = []
        for j in range(m):
            if (j + 1) % 2 == 1:
                x.append(i + 1 + j * n)
            else:
                x.append((j + 1) * n - i)
        rec.append(x)
    indent = max([len(str(max(x))) for x in rec])
    for i in rec:
        for j in i:
            print(f"{' ' * (indent - len(str(j)))}{j}", end=' ')
        print()


if __name__ == "__main__":
    main()