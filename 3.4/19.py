from itertools import product


def main():
    s = input()
    var = sorted(set(filter(str.isupper, s)))
    print(' '.join(var) + ' F')
    for p in product([0, 1], repeat=len(var)):
        loc = dict(zip(var, p))
        res = eval(s, {}, loc)
        print(' '.join(map(str, p)) + ' ' + str(int(res)))


if __name__ == "__main__":
    main()