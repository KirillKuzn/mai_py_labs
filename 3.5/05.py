from sys import stdin


def main():
    text = stdin.read().replace('\n', ' ')
    words = sorted(set(text.split()))
    for word in words:
        if word.lower() == word.lower()[::-1]:
            print(word)


if __name__ == "__main__":
    main()