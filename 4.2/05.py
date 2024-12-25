def to_string(*data, sep=' ', end='\n'):
    out = []
    for d in data:
        out.append(str(d))
    return sep.join(out) + end


def main():
    print(to_string(1, 2, 3))


if __name__ == "__main__":
    main()