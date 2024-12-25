def main():
    """Почти обратный отсчет"""

    n = int(input())
    m = int(input())
    for i in range(n, m - 1, -(int((n - m) / 3))):
        if i - int((n - m) / 3) >= m:
            print(f"{i};", end=' ')
        else:
            print(i)
    print('Старт!')


if __name__ == "__main__":
    main()
