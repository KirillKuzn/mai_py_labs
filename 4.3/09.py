def cycle(s):
    index = 0
    while True:
        yield s[index]
        index = (index + 1) % len(s)
        

def main():
    print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))


if __name__ == "__main__":
    main()