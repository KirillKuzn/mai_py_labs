def main():
    with open('secret.txt', encoding='UTF-8') as f:
        text = f.read()
        for s in text:
            print(chr(ord(s) % 128), end='')


if __name__ == "__main__":
    main()
