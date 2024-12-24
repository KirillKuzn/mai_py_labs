def main():
    f = int(input())
    last = int(input())
    if last > f: 
        for i in range(f, last + 1):
            print(i, end=' ')
    else:
        for i in range(f, last - 1, -1):
            print(i, end=' ')
    

if __name__ == "__main__":
    main()