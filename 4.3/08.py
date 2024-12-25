def fibonacci(n):
    n += 2
    n1 = 0
    n2 = 1
    for i in range(2, n):
        yield n1
        n1, n2 = n2, n1 + n2


def main():
    print(*fibonacci(10), sep=', ')


if __name__ == "__main__":
    main()