from itertools import product, permutations


def main():
    n = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    n.sort()
    m = ['пик', 'треф', 'бубен', 'червей']
    m.sort()
    c = list(product(n, m))
    ye = input()
    no = input()
    i = 0
    for p in permutations(c, 3):
        if (ye[:3] in str(p)) and (no not in str(p)):
            print(' '.join(p[0]), ' '.join(p[1]), ' '.join(p[2]), sep=', ')
            if i == 9:
                break
            i += 1


if __name__ == "__main__":
    main()