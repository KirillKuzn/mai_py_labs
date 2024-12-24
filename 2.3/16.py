def main():
    a = int(input())
    a = str(a)
    if len(a) % 2 == 0:
        s = ''
        while len(s) != len(a):
            s += a[-1]
            a = a[:-1]
        if a == s:
            print('YES')
        else:
            print('NO')
    else:
        s = ''
        while len(s) != len(a) - 1:
            s += a[-1]
            a = a[:-1]
        if a[:-1] == s:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main()