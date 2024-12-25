def prost(x):
    d = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d += 1
    if d == 1 and x > 1:
        return True
    else:
        return False


def main():
    n = int(input())
    c = 0
    for i in range(n):
        a = int(input())
        if prost(a):
            c += 1
    print(c)


if __name__ == "__main__":
    main()