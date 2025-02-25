class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split('/'))
        else:
            self.num, self.den = args
        if self.num * self.den < 0:
            self.sign = -1
        else:
            self.sign = 1
        self.num, self.den = abs(self.num), abs(self.den)
        self.__red()

    def numerator(self, number=None):
        if number is None:
            return self.num
        if number < 0:
            self.sign *= -1
        self.num = abs(number)
        self.__red()

    def denominator(self, number=None):
        if number is None:
            return self.den
        if number < 0:
            self.sign *= -1
        self.den = abs(number)
        self.__red()

    def __str__(self):
        return f"{self.sign * self.num}/{self.den}"
    
    def __repr__(self):
        return f"Fraction('{self.sign * self.num}/{self.den}')"

    def __gcd(self, a, b):
        a = abs(a)
        b = abs(b)
        while a % b != 0:
            a, b = b, a % b
        return b

    def __red(self):
        g = self.__gcd(self.num, self.den)
        self.num //= g
        self.den //= g
        return self

    def __neg__(self):
        return Fraction(-1 * self.sign * self.num, self.den)
    

