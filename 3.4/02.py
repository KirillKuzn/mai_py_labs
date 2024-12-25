def main():
    s1 = input().split(', ')
    s2 = input().split(', ')
    for i in list(zip(s1, s2)):
        print(i[0] + ' - ' + i[1])


if __name__ == "__main__":
    main()
