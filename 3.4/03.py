from itertools import count


def main():
    start, stop, step = map(float, input().split())
    for value in count(start, step):
        if value <= stop:
            print(round(value, 2))
        else:
            break


if __name__ == "__main__":
    main()