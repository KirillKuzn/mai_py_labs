def main():
    n = int(input())
    s = [input() for i in range(n)]
    for a in s:
        if 'зайка' in a:
            a = a.replace('зайка', '*')
            print(a.index('*') + 1)
        else:
            print('Заек нет =(')



if __name__ == "__main__":
    main()