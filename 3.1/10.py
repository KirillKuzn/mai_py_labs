def main():
    s = []
    a = input()
    while a != 'ФИНИШ':
        s.append(a)
        a = input()
    s = ''.join(s)
    orus = ord('а')
    oeng = ord('a')
    alphabet = ''.join([chr(i) for i in range(orus, orus + 32)]) + 'ё' + ''.join([chr(i) for i in range(oeng, oeng + 26)])
    ans = ''
    cmax = 0
    for letter in alphabet:
        if s.count(letter) + s.count(chr(ord(letter) - 32)) > cmax:
            cmax = s.count(letter) + s.count(chr(ord(letter) - 32))
            ans = letter
    print(ans)


if __name__ == "__main__":
    main()