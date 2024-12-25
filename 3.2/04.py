def main():
    n = int(input())
    m = int(input())
    nset = set()
    mset = set()
    for i in range(n):
        nset.add(input())
    for i in range(m):
        mset.add(input())
    c = nset & mset
    print(len(c)) if len(c) > 0 else print('Таких нет')


if __name__ == "__main__":
    main()