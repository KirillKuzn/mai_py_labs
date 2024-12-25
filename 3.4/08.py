def main():
    m = int(input())
    menu = []
    for i in range(m):
        menu.append(input())
    n = int(input())
    for i in range(n):
        print(menu[i % m])


if __name__ == "__main__":
    main()