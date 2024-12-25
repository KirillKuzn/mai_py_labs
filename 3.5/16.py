import sys


def main():
    search = input().lower()
    flag = False
    files = [line.strip() for line in sys.stdin]
    for file in files:
        with open(file, encoding='UTF-8') as f:
            text = f.read()
            text = ' '.join(text.lower().split())
            if search in text:
                print(file)
                flag = True
    if not flag:
        print("404. Not Found")


if __name__ == "__main__":
    main()