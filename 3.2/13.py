def main():
    n = int(input())
    menu = {}
    for i in range(n):
        menu[input()] = 0
    m = int(input())
    for i in range(m):
        c = int(input())
        for j in range(c):
            menu[input()] += 1
    a = []
    for d in menu:
        if menu[d] == 0:
            a.append(d)
    a.sort()
    if len(a) > 0:
        for d in a:
            print(d)
    else:
        print('Готовить нечего') 


if __name__ == "__main__":
    main()

