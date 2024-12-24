def main():
    z = 0
    a = input()
    while a != 'Приехали!':
        if 'зайка' in a:
            z += 1
        a = input()
    print(z)


if __name__ == "__main__":
    main()