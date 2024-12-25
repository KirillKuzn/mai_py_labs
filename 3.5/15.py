import json
import sys


def main():
    ans = [line.strip() for line in sys.stdin]
    score = 0
    with open('scoring.json', encoding='UTF-8') as file:
        d = json.load(file)
    patterns = []
    for test_group in d:
        ppt = test_group['points'] // len(test_group['tests'])
        for test in test_group['tests']:
            patterns.append((test['pattern'], ppt))
    for i in range(len(patterns)):
        if ans[i] == patterns[i][0]:
            score += patterns[i][1]
    print(score)


if __name__ == "__main__":
    main()