import string


def index(text):
    text = ''.join([s for s in text if s not in string.punctuation])
    symbols = sorted(set(text.replace(' ', '')))
    for s in symbols:
        yield (s, text.index(s))


def main():
    """Генератор индексов"""
    
    text = "Мама мыла раму"
    for letter, i in index(text):
        print(f"{letter}: {i}")

    text = "The quick brown fox jumps over a lazy dog."
    for letter, i in index(text):
        print(letter, i, sep="-", end=", ")


if __name__ == "__main__":
    main()