buff = []


def modern_print(s):
    if s not in buff:
        print(s)
        buff.append(s)


def main():
    modern_print('sdfjowf')
    modern_print('sdfjowf')
    modern_print('fqoggerj')


if __name__ == "__main__":
    main()