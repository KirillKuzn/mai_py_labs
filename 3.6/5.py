from sys import stdin
import json


def main():
    """Алфавитная статистика"""

    text = []
    filename = 'result.json'
    for line in stdin:
        text.append(line.rstrip("\n"))
    d = {}
    for w in text:
        for i in range(1, len(w), 2):
            if w[i].lower() not in d:
                d[w[i].lower()] = [w.lower()]
            else:
                d[w[i].lower()].append(w.lower())
    for k in d.keys():
        d[k] = list(sorted(set(d[k])))
    with open(filename, "w", encoding="UTF-8") as file_out:
        json.dump(d, file_out, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()