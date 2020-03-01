import math


class Vector:
    def __init__(self, values):
        self.V = tuple(values)
        self.dim = len(values)

    def __add__(self, other):
        return Vector([(V + W) for (V, W) in zip(self.V, other.V)])

    def __neg__(self):
        return Vector([-1 * V for V in self.V])

    def __sub__(self, other):
        return Vector([(V - W) for (V, W) in zip(self.V, other.V)])

    def __mul__(self, scalar):
        return Vector([V * scalar for V in self.V])

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        return Vector([V / scalar for V in self.V])

    def __str__(self):
        return str(self.V)

    def norm(self):
        s = 0
        for V in self.V:
            s += V * V
        return math.sqrt(s)

    def dot(self, other):
        s = 0
        for (V, W) in zip(self.V, other.V):
            s += V * W
        return s

    def proj(self, other):
        return (self * other.dot(self)) / (self.norm() ** 2)


class Polynomial:
    def __init__(self, coefficients):
        self.C = list(coefficients.values())
        self.P = list(coefficients.keys())
        self.l = len(coefficients)


u = Vector([1, 2, 3])
w = Vector([4, 5, -6])

print(u + w)
print(u - w)
print(3 * u)
print(u * 3)
print(-u)
print(u / 3)
print(u.norm())
print(u.dot(w))
print(u.proj(w))
