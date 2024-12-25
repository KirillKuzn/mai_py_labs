def main():
    n = int(input())
    ch = [int(input()) for i in range(n)]
    nod = 0
    for d in range(1, min(ch) + 1):
        for i in ch:
            if i % d != 0:
                break
        else:
            nod = max(nod, d)
    print(nod)


if __name__ == "__main__":
    main()