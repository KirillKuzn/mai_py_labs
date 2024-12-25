def main():
    n = int(input())
    s = [input() for i in range(n)]
    c = 0
    for a in s:
        c += a.count('зайка')
    print(c)


if __name__ == "__main__":
    main()