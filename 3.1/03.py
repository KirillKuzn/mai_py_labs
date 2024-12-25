def main():
    L = int(input())
    n = int(input())
    s = [input() for i in range(n)]
    for a in s:
        if len(a) > L:
            print(a[:L - 3] + '...')
        else:
            print(a)


if __name__ == "__main__":
    main()