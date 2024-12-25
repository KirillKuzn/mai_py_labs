from itertools import product


def main():
    n = int(input())
    s = [i for i in range(1, n + 1)]
    for p in product(s, repeat=2):
        print(p[0] * p[1], end=' ') if p[1] < s[-1] else print(p[0] * p[1])


if __name__ == "__main__":
    main()