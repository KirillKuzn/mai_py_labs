def main():
    """Особый минимум"""

    n = int(input())
    p = [int(input()) for i in range(n)]
    b = []
    for i in range(1, n):
        if p[i] > p[i - 1]:
            b.append(p[i])
    print(min(b))



if __name__ == "__main__":
    main()