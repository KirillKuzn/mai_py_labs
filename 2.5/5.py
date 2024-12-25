def main():
    """Сумма средних"""
    
    n = int(input())
    ans = 0
    for i in range(n):
        p = []
        a = input()
        while a != 'stop':
            p.append(int(a))
            a = input()
        ans += sum(p) / len(p)
    print(round(ans, 2))



if __name__ == "__main__":
    main()