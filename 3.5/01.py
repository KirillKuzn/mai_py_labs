from sys import stdin


def main():
    n = stdin.read().replace('\n', ' ')
    n = list(map(int, n.split()))
    print(sum(n))


if __name__ == "__main__":
    main()