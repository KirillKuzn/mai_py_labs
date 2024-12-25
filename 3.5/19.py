def main():
    shift = int(input())
    ans = ''
    with open('public.txt', encoding='UTF-8') as file_in:
        text = file_in.read()
        for s in text:
            if 65 <= ord(s) <= 90:
                ans += chr(65 + (ord(s) - 65 + shift) % (90 - 65 + 1))
            elif 97 <= ord(s) <= 122:
                ans += chr(97 + (ord(s) - 97 + shift) % 26)
            else:
                ans += s
    with open('private.txt', 'w', encoding='UTF-8') as out: 
        print(ans, file=out)


if __name__ == "__main__":
    main()