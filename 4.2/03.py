def gcd(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        ch = [i for i in numbers]
        nod = 0
        for d in range(1, min(ch) + 1):
            for i in ch:
                if i % d != 0:
                    break
            else:
                nod = max(nod, d)
        return nod


def main():
    print(gcd(36, 48, 156, 100500))


if __name__ == "__main__":
    main()