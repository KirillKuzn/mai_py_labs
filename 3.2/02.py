def main():
    s1 = input()
    s2 = input()
    b1 = set(s1)
    b2 = set(s2)
    print(''.join(b1 & b2))


if __name__ == "__main__":
    main()