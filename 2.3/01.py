def main():
    a = input()
    while a != 'Три!':
        print('Режим ожидания...')
        a = input()
    else:
        print('Ёлочка, гори!')


if __name__ == "__main__":
    main()