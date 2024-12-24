def main():
    b = int(input())
    a = int(input())
    a1, b1 = a, b
    while a % b != 0:
        a, b = b, a % b
    if b == 1:
        print(a1 * b1)
    else:
        print(b1 * a1 // b)


if __name__ == "__main__":
    main()