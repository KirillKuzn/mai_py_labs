def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    

def main():
    num = int(input())
    print(is_prime(num))


if __name__ == "__main__":
    main()