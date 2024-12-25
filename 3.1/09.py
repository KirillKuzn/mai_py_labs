def main():
    s = []
    a = input()
    while a:
        if '#' in a and a[0] != '#':
            s.append(a[:a.index('#')])
        if '#' not in a:
            s.append(a)
        a = input()
    for a in s:
        print(a)


if __name__ == "__main__":
    main()