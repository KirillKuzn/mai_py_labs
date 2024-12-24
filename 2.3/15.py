def main():
    n = int(input())
    c = 0
    for i in range(n):
        a = input()
        if 'зайка' in a:
            c += 1
    print(c)


if __name__ == "__main__":
    main()