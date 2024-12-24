def main():
    s = 0
    a = float(input())
    while a != 0:
        if a >= 500:
            s += a * 0.9
        else:
            s += a
        a = float(input())
    print(s)


if __name__ == "__main__":
    main()