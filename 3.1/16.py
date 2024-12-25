def main():
    L = int(input())
    n = int(input())
    title = [input() for i in range(n)]
    text = ''.join(title)
    t = '\n'.join(title)
    title = ''
    if len(text) > L - 3:
        c = 0
        for i in range(L - 3):
            if text[i] == t[i + c]:
                title += text[i]
            else:
                title += '\n' + text[i]
                c += 1
        text = title + '...'
    print(text)


if __name__ == "__main__":
    main()