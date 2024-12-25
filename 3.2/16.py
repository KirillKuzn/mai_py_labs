def main():
    s = input().split()
    ans = set()
    while s:
        for i in range(1, len(s)):
            if s[i] == 'зайка':
                ans.add(s[i - 1])
            if s[i - 1] == 'зайка':
                ans.add(s[i])
        s = input().split()
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()