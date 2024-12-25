def recursive_sum(*numbers):
    if not numbers:
        return 0
    return numbers[-1] + recursive_sum(*numbers[:-1])


def main():
    print(recursive_sum(1, 2, 3))


if __name__ == "__main__":
    main()