def main():
    n = int(input())
    m = int(input())
    d = {}
    for i in range(n + m):
        c = input()
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    s = []
    for c in d:
        if d[c] == 1:
            s.append(c)
    print(len(s)) if len(s) > 0 else print('Таких нет')


if __name__ == "__main__":
    main()