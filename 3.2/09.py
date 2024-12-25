def main():
    d = {}
    a = input()
    while a:
        s = a.split()
        for o in s:
            if o in d:
                d[o] += 1
            else:
                d[o] = 1
        a = input()
    for k in d:
        print(k, d[k])


if __name__ == "__main__":
    main()