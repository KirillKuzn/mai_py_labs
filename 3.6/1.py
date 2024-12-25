def main():
    """Шинковка строк"""
    
    n = int(input())
    s = [input() for i in range(n)]
    for p in s:
        p, a, b = p.split('^')
        a, b = int(a), int(b)
        step = len(p) % 4
        res = p[a:b:step]
        print(res)


if __name__ == "__main__":
    main()