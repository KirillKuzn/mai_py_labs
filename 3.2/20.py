def pr(x, y):
    a, b = max(x, y), min(x, y)
    while a % b != 0:
        a, b = b, a % b
    if b == 1:
        return True


def main():
    n = list(map(int, input().split('; ')))
    d = {}
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                if pr(n[j], n[i]):
                    if n[i] in d:
                        d[n[i]] += [n[j]]
                    else:
                        d[n[i]] = [n[j]]    
    num = []
    for k in d:
        s = list(set(d[k]))
        s.sort()
        d[k] = s
        num.append(k)
    num.sort()
    for i in num:
        print(str(i) + ' - ' + str(d[i]).replace('[', '').replace(']', ''))


if __name__ == "__main__":
    main()