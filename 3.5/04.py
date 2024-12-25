from sys import stdin


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    search = lines.pop(-1)
    for line in lines:
        if search.lower() in line.lower():
            print(line)


if __name__ == "__main__":
    main()