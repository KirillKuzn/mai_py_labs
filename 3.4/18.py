from itertools import product


def main():
    s = input()
    print('a b c f')
    for p in product([0, 1], repeat=3):
        a, b, c = p[0], p[1], p[2]
        if (eval(s)):
            print(a, b, c, 1)
        else:
            print(a, b, c, 0)


if __name__ == "__main__":
    main()