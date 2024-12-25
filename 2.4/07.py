def main():
    n = int(input())
    s = 3
    for i in range(1, n + 1):
        for j in range(s, 0, -1):
            print(f'До старта {j} секунд(ы)')
        print(f'Старт {i}!!!')
        s += 1


if __name__ == "__main__":
    main()