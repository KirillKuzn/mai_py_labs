def main():
    """Словарная опись"""

    d = {}
    t = []
    s = input()
    while s:
        t += s.split()
        s = input()
    for w in t:
        index = (len(w) // 2) - 1 + len(w) % 2
        key = w[index].lower()
        if key not in d:
            d[key] = [w.upper()]
        else:
            d[key].append(w.upper())
    for a in d.keys():
        print(a, '"' + '. '.join(sorted(set(d[a]))) + '"')


if __name__ == "__main__":
    main()