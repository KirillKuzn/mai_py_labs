def main():
    o = set()
    n = int(input())
    for i in range(n):
        s = input().split()
        for a in s:
            o.add(a)
    for ob in o:
        print(ob)


if __name__ == "__main__":
    main()