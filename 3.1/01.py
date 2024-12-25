def main():
    n = int(input())
    s = [input() for i in range(n)]
    for a in s:
        if a[0] not in 'абв':
            print('NO')
            break
    else:
        print('YES')


if __name__ == "__main__":
    main()
