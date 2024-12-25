def main():
    s = list(map(int, input().split()))
    nod = 0
    for i in range(1, min(s) + 1):
        for j in s:
            if j % i != 0:
                break
        else:
            nod = i
    print(nod)


if __name__ == "__main__":
    main()