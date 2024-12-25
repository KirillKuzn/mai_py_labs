def main():
    n = int(input())
    w = {}
    for i in range(n):
        c = list(map(int, input().split()))
        rc = f'{c[0] // 10} {c[1] // 10}'
        if rc in w:
            w[rc] += 1
        else:
            w[rc] = 1
    print(max(w.values()))


if __name__ == "__main__":
    main()