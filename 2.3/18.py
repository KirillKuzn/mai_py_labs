def main():
    n = int(input())
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                if n // i != 1:
                    print(f"{i} *", end=' ')
                else:
                    print(f"{i}")
                n //= i
                break


if __name__ == "__main__":
    main()