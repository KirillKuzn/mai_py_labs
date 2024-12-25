from itertools import product


def main():
    n = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    m = ['пик', 'треф', 'бубен', 'червей']
    s = input()
    m.remove(s)
    for p in product(n, m):
        print(p[0] + ' ' + p[1])


if __name__ == "__main__":
    main()