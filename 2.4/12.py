def main():
    n = int(input())
    m = int(input())
    rec = []
    for i in range(n):
        x = []
        for j in range(m):
            x.append(i * m + j + 1)
        rec.append(x)
    indent = max([len(str(max(x))) for x in rec])
    for i in rec:
        for j in i:
            print(f"{' ' * (indent - len(str(j)))}{j}", end=' ')
        print()


if __name__ == "__main__":
    main()