def main():
    d1 = {}
    s = input().split()
    people = []
    while s:
        if s[0] in d1:
            d1[s[0]] += [s[1]]
        else:
            d1[s[0]] = [s[1]]
        if s[1] in d1:
            d1[s[1]] += [s[0]]
        else:
            d1[s[1]] = [s[0]]
        people += s
        s = input().split()
    people = list(set(people))
    people.sort()
    d2 = {}
    for p in people:
        d2[p] = []
        for f in d1[p]:
            for nf in d1[f]:
                if nf != p and nf not in d1[p]:
                    d2[p] += [nf]
    for f in d2:
        snf = list(set(d2[f]))
        snf.sort()
        print(f + ': ' + ', '.join(snf))


if __name__ == "__main__":
    main()