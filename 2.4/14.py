def main():
    n = int(input())
    m = int(input())
    rec = []
    for i in range(n):
        x = []
        for j in range(m):
            x.append(i * m + 1 + j)
        if (i + 1) % 2 == 1:
            rec.append(x)
        else:
            rec.append(x[::-1])
    indent = max([len(str(max(x))) for x in rec])
    for i in rec:
        for j in i:
            print(f"{' ' * (indent - len(str(j)))}{j}", end=' ')
        print()


if __name__ == "__main__":
    main()