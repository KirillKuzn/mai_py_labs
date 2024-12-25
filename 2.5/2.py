def main():
    """Условное вычисление"""
    
    a = int(input())
    b = int(input())
    s = input()
    if len(s) % 6 == 0:
        print(a + b)
    elif len(s) % 3 == 0:
        print(a - b)
    elif len(s) % 2 == 0:
        print(a * b)
    else:
        print(a // b)



if __name__ == "__main__":
    main()