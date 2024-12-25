def main():
    n = int(input())
    d = {}
    for i in range(n):
        f = input()
        if f in d:
            d[f] += 1
        else:
            d[f] = 1
    if max(d.values()) == 1:
        print('Однофамильцев нет')
    else:
        s = []
        for f in d:
            if d[f] > 1:
                s.append(f'{f} - {d[f]}')
        s.sort()
        for li in s:
            print(li)


if __name__ == "__main__":
    main()