class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                if '/' in args[0]:
                    self.num, self.den = map(int, args[0].split('/'))
                else:
                    self.num = int(args[0])
                    self.den = 1
            else:
                self.num = args[0]
                self.den = 1
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

    def reverse(self):
        return Fraction(self.sign * self.den, self.num)

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

    def __lcm(self, a, b):
        a1, b1 = abs(a), abs(b)
        if self.__gcd(a, b) == 1:
            return a1 * b1
        return a1 * b1 // self.__gcd(a, b)

    def __red(self):
        g = self.__gcd(self.num, self.den)
        self.num //= g
        self.den //= g
        return self

    def __neg__(self):
        return Fraction(-1 * self.sign * self.num, self.den)
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            return Fraction(self.num * self.sign + other.num * other.sign, self.den)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            return Fraction(self.num * self.sign * x + other.num * other.sign * y, self.den * x)
        
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            return Fraction(self.num * self.sign - other.num * other.sign, self.den)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            return Fraction(self.num * self.sign * x - other.num * other.sign * y, self.den * x)
        
    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            return Fraction(self.num * self.sign + other.num * other.sign, self.den)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            return Fraction(self.num * self.sign * x + other.num * other.sign * y, self.den * x)
        
    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            return Fraction(-self.num * self.sign + other.num * other.sign, self.den)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            return Fraction(-self.num * self.sign * x + other.num * other.sign * y, self.den * x)
    
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            self.num = self.num * self.sign + other.num * other.sign
            self.sign = 1 if self.num >= 0 else -1
            self.num = abs(self.num)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            self.num, self.den = self.num * self.sign * x + other.num * other.sign * y, self.den * x
            self.sign = 1 if self.num >= 0 else -1
            self.num = abs(self.num)
        return self.__red()
    
    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            self.num = self.num * self.sign - other.num * other.sign
            self.sign = 1 if self.num >= 0 else -1
            self.num = abs(self.num)
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            self.num, self.den = self.num * self.sign * x - other.num * other.sign * y, self.den * x
            self.sign = 1 if self.num >= 0 else -1
            self.num = abs(self.num)
        return self.__red()
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * self.sign * other.num * other.sign, self.den * other.den)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * self.sign * other.den * other.sign, self.den * other.num)
    
    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * self.sign * other.num * other.sign, self.den * other.den)
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.den * self.sign * other.num * other.sign, self.num * other.den)
    
    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num = self.num * self.sign * other.num * other.sign
        self.sign = 1 if self.num >= 0 else -1
        self.num = abs(self.num)
        self.den *= other.den
        return self.__red()
    
    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num = self.num * self.sign * other.den * other.sign
        self.sign = 1 if self.num >= 0 else -1
        self.num = abs(self.num)
        self.den *= other.num
        return self.__red()

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            if self.num * self.sign < other.num * other.sign:
                return True
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            if self.num * self.sign * x < other.num * other.sign * y:
                return True
        return False
    
    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            if self.num * self.sign > other.num * other.sign:
                return True
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            if self.num * self.sign * x > other.num * other.sign * y:
                return True
        return False
    
    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            if self.num * self.sign <= other.num * other.sign:
                return True
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            if self.num * self.sign * x <= other.num * other.sign * y:
                return True
        return False
    
    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.den == other.den:
            if self.num * self.sign >= other.num * other.sign:
                return True
        else:
            x = self.__lcm(self.den, other.den) // self.den
            y = self.__lcm(self.den, other.den) // other.den
            if self.num * self.sign * x >= other.num * other.sign * y:
                return True
        return False
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.num == other.num and self.den == other.den:
            return True
        return False
    
    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if self.num != other.num or self.den != other.den:
            return True
        return False
    

# a = Fraction(1, 2)
# b = Fraction('2/3')
# c, d = map(Fraction.reverse, (3 - a, 2 / b))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)