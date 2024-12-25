from itertools import combinations


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for c in combinations(s, 2):
        print(c[0] + ' - ' + c[1])


if __name__ == "__main__":
    main()