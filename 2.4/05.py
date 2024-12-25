def main():
    n = int(input())
    c = 0
    for i in range(n):
        a = input()
        cm = 0
        while a != 'ВСЁ':
            if a == 'зайка':
                cm += 1
            a = input()
        if cm >= 1:
            c += 1
    print(c)


if __name__ == "__main__":
    main()