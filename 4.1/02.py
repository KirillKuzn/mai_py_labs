def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def main():
    print(gcd(12, 45))


if __name__ == "__main__":
    main()