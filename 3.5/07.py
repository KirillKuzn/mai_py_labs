def main():
    num = ''
    with open(input(), encoding='UTF-8') as file_in:
        num = file_in.read().replace('\n', ' ').split()
    pol = 0
    for i in range(len(num)):
        num[i] = int(num[i])
        if num[i] > 0:
            pol += 1
    print(len(num), pol, min(num), max(num), sum(num), round(sum(num) / len(num), 2), sep='\n')


if __name__ == "__main__":
    main()