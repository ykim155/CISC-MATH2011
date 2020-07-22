import matplotlib.pyplot as plt
import random
import math
import cmath

# Number 1
x = [x / 10.0 for x in range(-20, 11)]  # list of floats from -2 to 1
y = [xi ** 3 + xi ** 2 + 1 for xi in x]  # using values from x to create list of values from function

plt.axhline(0, color='black')  # adds a horizontal axis
plt.axvline(0, color='black')  # adds a vertical axis

plt.plot(x, y, 'k')  # plot x and y

plt.plot([0, -1.45], [0, 0], 'b')
plt.plot([-1.45, -0.75], [0, 1.15], 'b')
plt.plot([0, -0.75], [1, 1.15], 'b')
plt.plot([0, 0], [1, 0], 'b')

plt.show()

# Number 2
z = [complex(random.uniform(0, 20), random.uniform(0, 20)) for i in range(5)]  # generate list of random complex numbers
print(z)


def real(z):
    r = [zi.real for zi in z]
    return r


def imag(z):
    i = [zi.imag for zi in z]
    return i


r = real(z)
i = imag(z)

print(r)
print(i)


# Number 3
def GetBunnyCloudData():
    f = open("bunny_cloud.dat", "r")  # open bunny_cloud.dat for reading
    DATA = f.readlines()  # reads all lines of bunny_cloud.dat and puts them into a list

    z = []  # empty list

    for s in DATA:  # for every line in bunny_cloud.dat
        ss = s.split()  # split function assigned to variable ss

        a = float(ss[0])  # returns the first number of line as a float
        b = float(ss[1])  # returns the second number of line as a float

        z.append(a + b * 1j)  # append complex number with the first number being real and the second being imaginary

    return z  # returns list of complex numbers


zb = GetBunnyCloudData()
zh = [complex(0, 0), complex(0, 1), complex(0.5, 1.5), complex(1, 1), complex(1, 0), complex(0, 0)]

xh = [zhi.real for zhi in zh]
yh = [zhi.imag for zhi in zh]

plt.plot(real(zb), imag(zb), 'y.')  # constructing the bunny
plt.plot(xh, yh, 'y')  # constructing a house

plt.show()

# Number 4
c = 1 + 1j


def scale(z, c):
    scaled = z * c
    return scaled


def trans(z, z0):
    translated = z + z0
    return translated


def conju(z):
    c = [zi.conjugate() for zi in z]
    return c


def rotat(z, a):
    return z * cmath.exp(a * 1j)


print(scale(c, 3))
print(trans(c, 2 + 2j))
print(conju(z))
print(rotat(c, math.pi / 4))

# Number 5
plt.axhline(0, color='black')  # adds a horizontal axis
plt.axvline(0, color='black')  # adds a vertical axis

sb = [scale(zbi, 3) for zbi in zb]
sh = [scale(zhi, 3) for zhi in zh]
plt.plot(real(sb), imag(sb), 'r.')
plt.plot(real(sh), imag(sh), 'r')

tb = [trans(zbi, 1 - 2j) for zbi in zb]
th = [trans(zhi, 1 - 2j) for zhi in zh]
plt.plot(real(tb), imag(tb), 'b.')
plt.plot(real(th), imag(th), 'b')

cb = conju(zb)
ch = conju(zh)
plt.plot(real(cb), imag(cb), 'g.')
plt.plot(real(ch), imag(ch), 'g')

rb = [rotat(zbi, 3 * math.pi / 4) for zbi in zb]
rh = [rotat(zhi, 3 * math.pi / 4) for zhi in zh]
plt.plot(real(rb), imag(rb), 'k.')
plt.plot(real(rh), imag(rh), 'k')

plt.show()
