from sys import stdin


def main():
    ans = []
    for line in stdin:
        if '#' not in line:
            ans.append(line.rstrip('\n'))
        elif line[0] != '#':
            ans.append(line[:line.index('#')])
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()