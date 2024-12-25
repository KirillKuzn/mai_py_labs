def is_palindrome(o):
    if isinstance(o, (str, list, tuple)):
        return o == o[::-1]
    if isinstance(o, int):
        return str(o) == str(o)[::-1]
    

def main():
    print(is_palindrome(input()))
    print(is_palindrome(1233432))
    print(is_palindrome([1, 3, 2, 5, 1]))


if __name__ == "__main__":
    main()