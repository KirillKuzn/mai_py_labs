def main():
    s = input()
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c += 1
            if i == len(s) - 1:
                print(s[i], c)
        else:
            print(s[i - 1], c)
            c = 1
            if i == len(s) - 1:
                print(s[i], 1)


if __name__ == "__main__":
    main()