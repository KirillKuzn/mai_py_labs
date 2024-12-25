def make_list(len_list, value=0):
    return [value for i in range(len_list)]


def main():
    print(make_list(3, 1))


if __name__ == "__main__":
    main()