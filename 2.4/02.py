def main():
    n = int(input())
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            print(f"{y} * {x} = {y * x}")


if __name__ == "__main__":
    main()