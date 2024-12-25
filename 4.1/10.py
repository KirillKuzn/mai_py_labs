def merge(t1, t2):
    res = list(t1 + t2)
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return tuple(res)


def main():
    print(merge((1, 2), (3, 4, 5)))
    print(merge((7, 12), (1, 9, 50)))


if __name__ == "__main__":
    main()