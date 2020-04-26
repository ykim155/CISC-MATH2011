"""
import matplotlib.pyplot as plt
import cmath, math

pi = math.pi
exp = cmath.exp


def Real(z):
    r = [zi.real for zi in z]
    return r


def Imag(z):
    i = [zi.imag for zi in z]
    return i


def avg(l):
    return sum(l)/len(l)


a = [2*n*pi/20 for n in range(21)]
z = [0.5 + 1j + 0.2*exp(ai*1j) for ai in a]

plt.plot(Real(z), Imag(z), 'k')

x = Real(z)
xa = avg(x)
y = Imag(z)
ya = avg(y)
print(xa, ya, z)

for i in range(len(z)):
    print(i)
    a = z[i].real ** 2 + z[i].imag ** 2
    print(a)

plt.show()
"""
"""
s = 'Write a program that splits this sentence that you are reading into words, and then into characters for each word.'
s_split = s.split()
s_char = []
for word in s_split:
    temp = list(word)
    s_char.append(temp)
print(s_char)
"""
"""
s = 'Charles W Thurston specializes in solar energy in finance and in technological processes Key areas of focus for Charles are bifacial panels and solar tracking He has been active in the industry for 25 years living and working in locations ranging from Brazil to Papua New Guinea'
s_split = s.split()
dict = {word:[] for word in s_split}

for pos in range(len(s_split)):
    dict[s_split[pos]].append(pos)

print(dict)
"""


def f(x):
    i = 0
    while True:
        if pow(2, i) <= x < pow(2, i + 1):
            print("n = " + str(i))
            break
        elif pow(2, i) > x:
            i -= 1
        else:
            i += 1

