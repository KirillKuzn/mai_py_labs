import os
import math


def main():
    file = input()
    dir_path = os.path.dirname(__file__)
    size = os.path.getsize(dir_path + '/' + file)
    units = ['Б', 'КБ', 'МБ', 'ГБ']
    unit_index = 0
    while size >= 1024 and unit_index < 3:
        size = math.ceil(size / 1024)
        unit_index += 1
    print(str(size) + units[unit_index])


if __name__ == "__main__":
    main()