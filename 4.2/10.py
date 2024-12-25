def secret_replace(text, **replaces):
    for symbol, cipher in replaces.items():
        for i in range(text.count(symbol)):
            index = i % len(cipher)
            text = text.replace(symbol, cipher[index], 1)
    return text
        

def main():
    print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))


if __name__ == "__main__":
    main()