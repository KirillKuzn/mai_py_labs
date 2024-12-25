def split_numbers(nums):
    return tuple(map(int, nums.split()))


def main():
    print(split_numbers(input()))


if __name__ == "__main__":
    main()