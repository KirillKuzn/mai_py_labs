def search(mn, mx):
        n = (mn + mx + 1) // 2
        print(n)
        status = input()
        if status == 'Больше':
            return search(n, mx)
        elif status == 'Меньше':
            return search(mn, n)
        else:
            return n


def main():
    print(search(0, 1000))


if __name__ == "__main__":
    main()