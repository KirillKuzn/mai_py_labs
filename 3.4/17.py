from itertools import product, combinations, chain


def main():
    m = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
    n = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
    name = input()
    value = input()
    n.remove(value)
    cards = product(n, m.values())
    combs = sorted(combinations(cards, 3))
    res = [row for row in combs if m[name] in chain.from_iterable(row)]
    pos = tuple(tuple(i.split()) for i in input().split(", "))
    flag = 0
    for i in res:
        if flag:
            print(', '.join(f'{rank} {suit}' for rank, suit in i))
            break
        if pos == i:
            flag += 1


if __name__ == "__main__":
    main()