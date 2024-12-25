def main():
    s = []
    a = input()
    while a:
        if a[-3:] == '@@@':
            a = input()
        elif a[:2] == '##':
            s.append(a[2:])
            a = input()
        else:
            s.append(a)
            a = input()
    for a in s:
        print(a)


if __name__ == "__main__":
    main()