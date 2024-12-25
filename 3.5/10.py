def main():
    f = input()
    n = int(input())
    with open(f, encoding='UTF-8') as file:
        text = file.readlines()
    for s in text:
        s = s.rstrip('\n')
    for i in range(n, 0, -1):
        print(text[-i], end='')


if __name__ == "__main__":
    main()