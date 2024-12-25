def main():
    n = int(input())
    v = 0
    el = 1
    stairs = []
    while v < n:
        s = ''
        for j in range(el):
            v += 1
            s = s + str(v) + ' '
            if v == n:
                break
        else:
            el += 1
        stairs.append(s)
    lmax = len(stairs[-1])
    for i in range(el):
        print(f"{stairs[i]: ^{lmax}}")
        

if __name__ == "__main__":
    main()