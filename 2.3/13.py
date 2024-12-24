def main():
    n = int(input())
    f = 'ЯЯЯЯЯ'
    for i in range(n):
        a = input()
        f = min(a, f)
    print(f)


if __name__ == "__main__":
    main()