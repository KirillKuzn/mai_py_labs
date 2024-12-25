def main():
    n = int(input())
    d = {}
    for i in range(n):
        ch = input()
        d[ch[:ch.index(':')]] = ch[ch.index(':') + 2:].split(', ')
    ans = []
    rd = {}
    for c in d:
        d[c] = set(d[c])
        for o in d[c]:
            if o in rd:
                rd[o].update({c})
            else:
                rd[o] = {c}
    for t in rd:
        if len(rd[t]) == 1:
            ans.append(t)
    ans.sort()
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()