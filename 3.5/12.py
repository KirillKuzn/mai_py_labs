def main():
    files = []
    for i in range(4):
        files.append(input())
    even = []
    odd = []
    eq = []
    with open(files[0], encoding='UTF-8') as nums:
        for row in nums:
            rev, rod, req = [], [], []
            for n in row.rstrip('\n').split():
                ch, nch = 0, 0
                for x in n:
                    if x in '02468':
                        ch += 1
                    if x in '13579':
                        nch += 1
                if ch > nch:
                    rev.append(n)
                elif ch < nch:
                    rod.append(n)
                else:
                    req.append(n)
            even.append(' '.join(rev))
            odd.append(' '.join(rod))
            eq.append(' '.join(req))
    with open(files[1], 'w', encoding='UTF-8') as out1:
        for r in even:
            print(r, file=out1)
    with open(files[2], 'w', encoding='UTF-8') as out2:
        for r in odd:
            print(r, file=out2)
    with open(files[3], 'w', encoding='UTF-8') as out3:
        for r in eq:
            print(r, file=out3)


if __name__ == "__main__":
    main()