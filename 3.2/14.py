def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(input())
    m = int(input())
    ans = []
    for i in range(m):
        name = input()
        c = int(input())
        ingr = []
        for j in range(c):
            pr = input()
            if pr in p:
                ingr.append(pr)
        if len(ingr) == c:
            ans.append(name)
    if len(ans) > 0:
        ans.sort()
        for a in ans:
            print(a)
    else:
        print('Готовить нечего')


if __name__ == "__main__":
    main()