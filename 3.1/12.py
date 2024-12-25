def main():
    kussia = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
    n = int(input())
    for i in range(n):
        print(kussia[i % 5])


if __name__ == "__main__":
    main()