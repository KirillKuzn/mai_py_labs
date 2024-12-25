def main():
    n = int(input())
    d = {}
    for i in range(n):
        inf = input().split()
        if len(inf) >= 3:
            d[inf[0]] = ' '.join(inf[1:])
        else:
            d[inf[0]] = inf[1]
    s = input()
    ans = []
    for c in d:
        if s in d[c]:
            ans.append(c)
    if len(ans) > 0:
        ans.sort()
        for a in ans:
            print(a)
    else:
        print('Таких нет')


if __name__ == "__main__":
    main()