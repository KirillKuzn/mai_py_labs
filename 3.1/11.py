def main():
    n = int(input())
    zag = [input() for i in range(n)]
    zap = input()
    for a in zag:
        if zap.lower() in a.lower():
            print(a)


if __name__ == "__main__":
    main()