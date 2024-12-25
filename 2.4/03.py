def main():
    n = int(input())
    v = 0
    el = 1
    while v < n:
        for j in range(el):
            v += 1
            print(v, end=' ')
            if v == n:
                break
        print()
        el += 1
    

if __name__ == "__main__":
    main()