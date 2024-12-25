def main():
    n = int(input())
    s = []
    for i in range(n):
        a = int(input())
        s.append(a)
    p = int(input())
    for i in s:
        print(i ** p)


if __name__ == "__main__":
    main()