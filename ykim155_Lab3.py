import math


class rational:

    def __init__(self, m, n):
        k = math.gcd(m, n)
        M = m // k
        N = n // k

        SGN = n // abs(n)

        self.NU = M * SGN
        self.DE = abs(N)

    def __str__(self):
        if self.DE == 1:
            msg = str(self.NU)
        else:
            m, n = self.NU, self.DE
            num, den = str(m), str(n)
            Nn, Nd = len(num), len(den)

            slack = max([(Nd - Nn) // 2, 0])  # could improve this to make it look nice in all cases
            top = slack * ' ' + num + slack * ' '

            slack = max([(Nn - Nd) // 2, 0])
            bot = slack * ' ' + den + slack * ' '

            msg = top + '\n' + '-' * max([Nn, Nd]) + '\n' + bot
        return msg

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        if rational.__instancecheck__(other):
            m1, m2 = self.NU, other.NU
            n1, n2 = self.DE, other.DE
            return rational(m1 * m2, n1 * n2)
        elif type(other) == int:
            return rational(self.NU * other, self.DE)
        else:
            raise TypeError('Multiplication of rational with non-rational or non-integer type')

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        if rational.__instancecheck__(other):
            m1, m2 = self.NU, other.NU
            n1, n2 = self.DE, other.DE
            return rational(n2 * m1 + n1 * m2, n1 * n2)
        elif type(other) == int:
            a = rational(other, 1)
            return self + a
        else:
            raise TypeError('Addition of rational with non-rational or non-integer type.')

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return rational(-self.NU, self.DE)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        if type(other) == int:
            a = rational(other, 1)
            return a - self
        else:
            raise TypeError('Subtraction of rational with non-rational or non-int type.')

    def __truediv__(self, other):
        if rational.__instancecheck__(other):
            m1, m2 = self.NU, other.NU
            n1, n2 = self.DE, other.DE
            return rational(m1 * n2, n1 * m2)  # what if other is an integer
        elif type(other) == int:
            a = rational(other, 1)
            return self / a
        else:
            raise TypeError('Division of rational with non-rational or non-integer type.')

    def __rtruediv__(self, other):
        if type(other) == int:
            a = rational(other, 1)
            return a / self
        else:
            raise TypeError('Division of rational with non-rational or non-integer type.')



class Zp:
    p = 13  # class attribute
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    def __init__(self, n):
        if n < 0:
            self.n = n % (-Zp.p)
        else:
            self.n = n % Zp.p  # instance attribute

    def __str__(self):
        p_sub = str(Zp.p).translate(Zp.subscript)
        msg = '[' + str(self.n) + ']' + p_sub
        return msg

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        if Zp.__instancecheck__(other):
            return Zp(self.n * other.n)
        elif type(other) == int or type(other) == float:
            return Zp(self.n * other)
        else:
            raise TypeError('Multiplication of Zp with a non-Zp or non-integer type.')

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        if Zp.__instancecheck__(other):
            return Zp(self.n + other.n)
        elif type(other) == int or type(other) == float:
            return Zp(self.n + other)
        else:
            raise TypeError('Addition of Zp with non-Zp or non-integer type.')

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Zp(-self.n)

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        if type(other) == int:
            return Zp(other - self.n)
        else:
            raise TypeError('Subtraction of Zp with non-Zp or non-integer type.')

    def __pow__(self, pr):
        n = self.n
        result = 1
        for i in range(pr):
            result *= n % Zp.p
        return Zp(result)

    def inv(self):
        # inv(a) = a^(-1) = a^(p-2) because a^(p-1) = 1 mod p
        return self ** (Zp.p - 2)

    def __truediv__(self, other):
        if Zp.__instancecheck__(other):
            return self * other.inv()
        elif type(other) == int or type(other) == float:
            return Zp(self.n / other)
        else:
            raise TypeError('Division of Zp with a non-Zp or non-integer')

    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            return Zp(other / self.n)
        else:
            raise TypeError('Division of Zp with a non-Zp or non-integer')


class polynomial:
    signs = {-1: ' - ', 1: ' + '}

    def __init__(self, P, A):
        pre_dict = {p: 0 for (p, a) in zip(P, A)}
        for (p, a) in zip(P, A):
            if a != 0:
                pre_dict[p] += a
        self.poly_dict = {p: a for (p, a) in pre_dict.items() if a != 0}
        self.sign_dict = {a: polynomial.signs[a/abs(a)] for a in self.poly_dict.values()}

    def __str__(self):
        msg = ''
        for (p, s) in zip(self.poly_dict.keys(), self.sign_dict.values()):
            a = self.poly_dict[p]
            msg = msg + s + str(abs(a)) + 'x^' + str(p)
        clean = msg[2:]
        clean = clean.replace('x^0', '')
        clean = clean.replace('x^1', 'x')
        return clean

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if polynomial.__instancecheck__(other):
            P = list(self.poly_dict.keys()) + list(other.poly_dict.keys())
            A = list(self.poly_dict.values()) + list(other.poly_dict.values())
            return polynomial(P, A)
        elif type(other) == int or type(other) == float:
            P = list(self.poly_dict.keys())
            A = list(self.poly_dict.values())
            P.append(0)
            A.append(other)
            return polynomial(P, A)
        else:
            raise TypeError('Addition of polynomial with non-polynomial or non-numerical type.')

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        P = list(self.poly_dict.keys())
        A = [-1 * a for a in self.poly_dict.values()]
        return polynomial(P, A)

    def __sub__(self, other):
        self + -other

    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            -self + other
        else:
            raise TypeError('Subtraction of polynomial with non-polynomial or non-numerical type.')

    def __mul__(self, other):
        if polynomial.__instancecheck__(other):
            P, Q = self.poly_dict.keys(), other.poly_dict.keys()
            A, B = self.poly_dict.values(), other.poly_dict.values()

            R = [p + q for p in P for q in Q]  # new powers
            C = [a * b for a in A for b in B]  # new coefficients

            return polynomial(R, C)
        elif type(other) == int or type(other) == float:
            P = list(self.poly_dict.keys())
            A = [other * a for a in self.poly_dict.values()]
            return polynomial(P, A)
        else:
            raise TypeError('Multiplication of polynomial with non-polynomial or non-numerical type.')

    def __rmul__(self, other):
        return self.__mul__(other)