def make_equation(*args) -> str:
    if len(args) == 1:
        return str(args[0])
    result = make_equation(*args[:-1])
    return f'({result}) * x + {args[-1]}'


def main():
    print(make_equation(3, 2, 1))


if __name__ == "__main__":
    main()