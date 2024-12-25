from itertools import *


def main():
    """Словарный комбинатор"""
    
    s = sorted(set(input().split('; ')))
    r = int(input())
    for p in permutations(s, r):
        print(''.join(p))


if __name__ == "__main__":
    main()