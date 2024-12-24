def main():
    b = int(input())
    a = int(input())
    while a % b != 0:
        a, b = b, a % b
    print(b)


if __name__ == "__main__":
    main()