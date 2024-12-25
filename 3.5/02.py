from sys import stdin


def main():
    ch = []
    avg = []
    for line in stdin:
        ch.append(line.rstrip('\n'))
    for p in ch:
        p = p.split()
        p[-2] = int(p[-1]) - int(p[-2])
        p.pop(-1)
        avg.append(p[-1])
    print(round(sum(avg) / len(avg)))


if __name__ == "__main__":
    main()