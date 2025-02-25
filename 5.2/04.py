def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split('/'))
        else:
            self.num, self.den = args
        self.__red()

    def numerator(self, number=None):
        if number is None:
            return self.num
        else:
            self.num = number
            self.__red()

    def denominator(self, number=None):
        if number is None:
            return self.den
        else:
            self.den = number
            self.__red()

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
    
    def __red(self):
        if gcd(self.num, self.den) > 1:
            b = self.num
            self.num //= gcd(self.num, self.den)
            self.den //= gcd(b, self.den)
        return self