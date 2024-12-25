def main():
    file1, file2 = input(), input()
    with open(file1, encoding='UTF-8') as file_in:
        with open(file2, 'w', encoding='UTF-8') as file_out:
            for line in file_in:
                line = line.strip().replace('\t', '')
                words = line.split()
                if len(words) != 0:
                    print(*words, file=file_out)


if __name__ == "__main__":
    main()