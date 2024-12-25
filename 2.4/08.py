def main():
    n = int(input())
    maxs = 0
    winner = ''
    for i in range(n):
        name = input()
        ch = int(input())
        s = 0
        while ch != 0:
            s += ch % 10
            ch //= 10
        if s >= maxs:
            maxs = s
            winner = name
    print(winner)


if __name__ == "__main__":
    main()