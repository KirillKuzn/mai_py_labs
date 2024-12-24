def main():
    a = int(input())
    amax = 0
    while a != 0:
        amax = max(amax, a % 10)
        a //= 10
    print(amax)



if __name__ == "__main__":
    main()