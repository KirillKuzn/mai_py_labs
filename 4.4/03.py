def count_pairs(*numbers, div=10):
    count = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                count += 1
    return count


def main():
    """Кратный подсчёт"""

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = count_pairs(*numbers)
    print(result)

    numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
    result = count_pairs(*numbers, div=3)
    print(result)

if __name__ == "__main__":
    main()