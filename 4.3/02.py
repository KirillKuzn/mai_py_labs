def recursive_digit_sum(num):
    if num > 0:
        return num % 10 + recursive_digit_sum(num // 10)
    else:
        return 0


def main():
    print(recursive_digit_sum(213532))


if __name__ == "__main__":
    main()