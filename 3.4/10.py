from itertools import product


def main():
    n = int(input())
    s = [str(i) for i in range(1, n - 1)]
    print('А Б В')
    for p in product(s, repeat=3):
        sm = 0
        for i in p:
            sm += int(i)
        if sm == n:
            print(' '.join(p))


if __name__ == "__main__":
    main()