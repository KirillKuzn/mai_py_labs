def make_matrix(size, value=0):
    result = []
    if isinstance(size, tuple):
        for y in range(size[1]):
            result.append([value for x in range(size[0])])
    else:
        for x in range(size):
            result.append([value for x in range(size)])
    return result


def main():
    print(make_matrix(4))


if __name__ == "__main__":
    main()