import json
from sys import stdin


def main():
    file = input()
    with open(file, encoding='UTF-8') as f:
        d = json.load(f)
    for line in stdin:
        key, value = line.strip().split(' == ')
        d[key] = value
    with open(file, 'w', encoding='UTF-8') as out:
        json.dump(d, out, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()