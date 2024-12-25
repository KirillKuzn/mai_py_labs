def main():
    s = list(map(int, input().split()))
    ans = []
    for i in s:
        a = bin(i)[2:]
        d = {}
        d['digits'] = len(a)
        d['units'] = a.count('1')
        d['zeros'] = a.count('0')
        ans.append(d)
    print(ans)


if __name__ == "__main__":
    main()