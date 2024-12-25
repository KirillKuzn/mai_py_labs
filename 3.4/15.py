from itertools import permutations


def main():
    n = int(input())
    s = []
    for i in range(n):
        s += input().split(', ')
    s.sort()
    for p in permutations(s, 3):
        print(' '.join(p))


if __name__ == "__main__":
    main()