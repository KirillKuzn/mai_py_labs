def main():
    s = input().split()
    for i in range(1, len(s) + 1):
        print(f"{i}. {s[i - 1]}")


if __name__ == "__main__":
    main()