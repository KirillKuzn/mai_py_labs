def main():
    a = input().lower().replace(' ', '')
    if a == a[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()