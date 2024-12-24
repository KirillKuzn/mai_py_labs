def main():
    a = int(input())
    if a == 1:
        print('NO')
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                print('NO')
                break
        else:
            print('YES')


if __name__ == "__main__":
    main()