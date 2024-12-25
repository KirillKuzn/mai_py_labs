def main():
    s = list(map(int, input().split()))
    p = int(input())
    for i in s:
        print(i ** p, end=' ')


if __name__ == "__main__":
    main()